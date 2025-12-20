# src/chess/team/builder.builder.py

"""
Module: chess.team.builder.builder
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.piece import UniquePieceDataService
from chess.schema import Schema, SchemaLookup
from chess.agent import PlayerAgent, AgentService
from chess.arena import Arena, ArenaService, ExcessiveTeamsInArenaException
from chess.team import (
    AddingDuplicateTeamException, Team, TeamBuildFailedException, TeamContext, TeamInsertionFailedException
)
from chess.system import Builder, BuildResult, IdentityService, InsertionResult, LoggingLevelRouter, id_emitter


class TeamBuilder(Builder[Team]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce Team instances whose integrity is always guaranteed.
     2.  Manage construction of Team instances that can be used safely by the client.
     3.  Ensure params for Team creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
     None

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            arena: Arena,
            schema: Schema,
            player_agent: PlayerAgent,
            id: int = id_emitter.team_id,
            schema_lookup: SchemaLookup = SchemaLookup(),
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService(),
            player_agent_service: AgentService = AgentService(),
    ) -> BuildResult[Team]:
        """
        # ACTION:
        1.  Check ID safety with IdentityService.validate_id.
        2.  Check schema correctness with SchemaLookup's number_bounds_validator.
        3.  Check player_agent safety with PlayAgentService.validate_player.
        4.  If any check fails, return the exception inside a BuildResult.
        5.  When all checks create a new Team object.
        6.  If the team is not in actor's team_assignments use their team_stack to add it.
    
        # PARAMETERS:
            *   id (int)
            *   player_agent (PlayerAgent)
            *   team_schema (Schema)
            *   identity_service (IdentityService)
            *   player_agent_service (AgentService)
            *   schema_validator (TeamSchemaValidator)
        All Services have default values to ensure they are never null.
        
        # Returns:
        BuildResult[Team] containing either:
            - On success: Team in the payload.
            - On failure: Exception.
    
        RAISES:
            *   TeamBuildFailedException
        """
        method = "TeamBuilder.builder"
        try:
            # Certify the build resources are safe to use.
            id_validation = identity_service.validate_id(id)
            if id_validation.is_failure:
                return BuildResult.failure(id_validation.exception)
            
            schema_validation = schema_lookup.schema_validator.validate(schema)
            if schema_validation.is_failure:
                return BuildResult.failure(schema_validation.exception)
            
            player_agent_validation = player_agent_service.validator.validate(player_agent)
            if player_agent_validation.is_failure:
                return BuildResult.failure(player_agent_validation.exception)
            
            arena_validation = arena_service.item_validator.validate(arena)
            if arena_validation.is_failure:
                return BuildResult.failure(arena_validation.exception)
            # If there's already two teams in the arena you cannot build another one.
            if arena.team_service.size > 1:
                return BuildResult.failure(
                    ExcessiveTeamsInArenaException(f"{method}: {ExcessiveTeamsInArenaException.DEFAULT_MESSAGE}")
                )
        
            # If no errors are detected build the Team object.
            team = Team(
                id=id,
                arena=arena,
                schema=schema,
                player_agent=player_agent,
                roster=UniquePieceDataService(),
                hostages=UniquePieceDataService(),
            )
            
            # Make sure the owning side of the team-player_agent relationship is set.
            insertion_result = cls._register_team_with_agent(agent=player_agent, team=team)
            if insertion_result.is_failure:
                return BuildResult.failure(insertion_result.exception)
            
            # Make sure the owning side of the tea-arena relationship is set.
            insertion_result = cls._insert_team_in_arena(arena=arena, team=team)
            if insertion_result.is_failure:
                return BuildResult.failure(insertion_result.exception)
                
            # Send the successfully built and registered Team object inside a BuildResult.
            return BuildResult.success(team)
        
        # Finally return a BuildResult containing any unhandled exception insided an
        # TeamBuildFailedException
        except Exception as ex:
            return BuildResult.failure(
                TeamBuildFailedException(ex=ex, message=f"{method}: {TeamBuildFailedException.DEFAULT_MESSAGE}")
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _register_team_with_agent(cls, team: Team, agent: PlayerAgent,) -> InsertionResult[Team]:
        """
        # ACTION:
        1.  After ensuring the team does not exist in the PlayerAgent's team_assignments push the Team onto the stack.

        # PARAMETERS:
            *   team (Team)
            *   agent (PlayerAgent)

        # Returns:
        InsertionResult[Team] containing either:
            - On success: Team in the payload.
            - On failure: Exception.

        RAISES:
            *   AddingDuplicateTeamException
            *   TeamInsertionFailedException
        """
        method = "TeamBuilder._register_team_with_agent"
        try:
            # See if the team is already in PlayerAgent's roster. It really shouldn't be.
            search = agent.team_assignments.search_teams(context=TeamContext(id=team.id))
            
            # Handle the case the search raised an error.
            if search.is_failure:
                return InsertionResult.failure(search.exception)
            # If the search gives a hit the Team has already been created. Send an error in the InsertionResult.
            if search.is_success:
                return InsertionResult.failure(
                    AddingDuplicateTeamException(f"{method}: {AddingDuplicateTeamException.DEFAULT_MESSAGE}")
                )
            # An empty search result is the happy path where the push occurs.
            if search.is_empty:
                return agent.team_assignments.add_team(team)
        
        # Finally return a InsertionResult containing any unhandled exception insided an
        # TeamInsertionFailedException
        except Exception as ex:
            return InsertionResult.failure(
                TeamInsertionFailedException(
                    ex=ex, message=f"{method}: {TeamInsertionFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _insert_team_in_arena(cls, arena: Arena, team: Team) -> InsertionResult[Team]:
        """
        # ACTION:
        1.  After ensuring the team does not exist in the PlayerAgent's team_assignments push the Team onto the stack.

        # PARAMETERS:
            *   team (Team)
            *   agent (PlayerAgent)

        # Returns:
        InsertionResult[Team] containing either:
            - On success: Team in the payload.
            - On failure: Exception.

        RAISES:
            *   AddingDuplicateTeamException
            *   TeamInsertionFailedException
        """
        method = "TeamBuilder._insert_team_in_arena"
        try:
            # An Arena has only two teams with different colors. We need to make sure the colors are different
            # The color search is the best fit for this process.
            search = arena.team_service.search_teams(context=TeamContext(color=team.schema.color))
            
            # Handle the case the search raised an error.
            if search.is_failure:
                return InsertionResult.failure(search.exception)
            # If the search gives a hit the Arena is probably full. Send an error in the InsertionResult.
            if search.is_success:
                return InsertionResult.failure(
                    ExcessiveTeamsInArenaException(
                        f"{method}: {ExcessiveTeamsInArenaException.DEFAULT_MESSAGE}"
                    )
                )
            # An empty search result is the happy path where the push occurs.
            if search.is_empty:
                return arena.team_service.add_team(team)
            
        # Finally return a InsertionResult containing any unhandled exception insided an
        # TeamInsertionFailedException
        except Exception as ex:
            return InsertionResult.failure(
                TeamInsertionFailedException(
                    ex=ex, message=f"{method}: {TeamInsertionFailedException.DEFAULT_MESSAGE}"
                )
            )