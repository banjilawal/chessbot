# src/chess/team/builder.builder.py

"""
Module: chess.team.builder.builder
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.agent import PlayerAgent, PlayerAgentService
from chess.arena import Arena, ArenaService, PlayingFieldOverCapacityException
from chess.piece import UniquePieceDataService
from chess.team import (
    Team, TeamBuildFailedException, TeamContext, TeamInsertionFailedException, TeamSchema, TeamSchemaLookup
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
            team_schema: TeamSchema,
            player_agent: PlayerAgent,
            id: int = id_emitter.team_id,
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService(),
            schema_service: TeamSchemaLookup = TeamSchemaLookup(),
            player_agent_service: PlayerAgentService = PlayerAgentService(),
    ) -> BuildResult[Team]:
        """
        # ACTION:
        1.  Check ID safety with IdentityService.validate_id.
        2.  Check team_schema correctness with TeamSchemaValidator.validate.
        3.  Check player_agent safety with PlayAgentService.validate_player.
        4.  If any check fails, return the exception inside a BuildResult.
        5.  When all checks create a new Team object.
        6.  If the team is not in actor's team_assignments use their team_stack to add it.
    
        # PARAMETERS:
            *   id (int)
            *   player_agent (PlayerAgent)
            *   team_schema (Schema)
            *   identity_service (IdentityService)
            *   player_agent_service (PlayerAgentService)
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
            
            schema_validation = schema_service.validator.validate(team_schema)
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
                    PlayingFieldOverCapacityException(f"{method}: {PlayingFieldOverCapacityException.DEFAULT_MESSAGE}")
                )
        
            # If no errors are detected build the Team object.
            team = Team(
                id=id,
                arena=arena,
                player_agent=player_agent,
                schema=team_schema,
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
        
        # Finally return a BuildResult containing any unhandled exceptions insided an
        # TeamBuildFailedException
        except Exception as ex:
            return BuildResult.failure(
                TeamBuildFailedException(ex=ex, message=f"{method}: {TeamBuildFailedException.DEFAULT_MESSAGE}")
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _register_team_with_agent(cls, agent: PlayerAgent, team: Team) -> InsertionResult[Team]:
        """"""
        method = "TeamBuilder._register_team_with_agent"
        try:
            search_result = agent.team_assignments.search_teams(context=TeamContext(id=team.id))
            if search_result.is_failure:
                return BuildResult.failure(search_result.exception)
            if search_result.is_empty:
                agent.team_assignments.add_team(team)
        except Exception as ex:
            return InsertionResult.failure(
                TeamInsertionFailedException(ex=ex, message=f"{method}: {TeamInsertionFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _insert_team_in_arena(cls, arena: Arena, team: Team) -> InsertionResult[Team]:
        """"""
        method = "TeamBuilder._insert_team_in_arena"
        try:
            # Search by color to ensure there's no team with the same color.
            search_result = arena.team_service.search_teams(context=TeamContext(color=team.schema.color))
            if search_result.is_failure:
                return BuildResult.failure(search_result.exception)
            if search_result.is_empty:
                arena.team_service.add_team(team)
        except Exception as ex:
            return InsertionResult.failure(
                TeamInsertionFailedException(ex=ex, message=f"{method}: {TeamInsertionFailedException.DEFAULT_MESSAGE}")
            )