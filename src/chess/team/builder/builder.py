# src/chess/team/builder.builder.py

"""
Module: chess.team.builder.builder
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.agent import Agent, AgentService
from chess.arena import Arena, ArenaService
from chess.piece import PieceContext, PieceFactory, UniquePieceDataService
from chess.system import Builder, BuildResult, IdentityService, InsertionResult, LoggingLevelRouter, id_emitter
from chess.team import Team, TeamBuildFailedException, TeamSchema, TeamSchemaService

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
         *   TeamBuilder

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            agent: Agent,
            arena: Arena,
            team_schema: TeamSchema,
            id: int = id_emitter.team_id,
            arena_service: ArenaService = ArenaService(),
            agent_service: AgentService = AgentService(),
            idservice: IdentityService = IdentityService(),
            schema_service: TeamSchemaService = TeamSchemaService(),
    ) -> BuildResult[Team]:
        """
        # ACTION:
        1.  Check ID safety with IdentityService.validate_id.
        2.  Check team_schema correctness with TeamSchemaValidator.validate.
        3.  Check agent safety with PlayAgentService.validate_player.
        4.  If any check fails, return the exception inside a BuildResult.
        5.  When all checks create a new Team object.
        6.  If the team is not in actor's team_assignments use their team_stack to add it.
    
        # PARAMETERS:
            *   id (int)
            *   agent (Agent)
            *   team_schema (TeamSchema)
            *   identity_service (IdentityService)
            *   agent_service (AgentService)
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
            id_validation = idservice.validate_id(id)
            if id_validation.is_failure:
                return BuildResult.failure(id_validation.exception)
            
            schema_validation = schema_service.validator.validate(team_schema)
            if schema_validation.is_failure:
                return BuildResult.failure(schema_validation.exception)
            
            agent_validation = agent_service.validator.validate(agent)
            if agent_validation.is_failure:
                return BuildResult.failure(agent_validation.exception)
            
            arena_validation = arena_service.item_validator.validate(arena)
            if arena_validation.is_failure():
                return BuildResult.failure(arena_validation.exception)
            
            
            # If no errors are detected build the Team object.
            team = Team(
                id=id,
                arena=arena,
                agent=agent,
                schema=team_schema,
                roster=UniquePieceDataService(),
                hostages=UniquePieceDataService(),
            )
            
            # If the team is not in Agent.team_assignments register it.
            if team not in agent.team_assignments:
                agent.team_assignments.push_unique_item(team)
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
    def _fill_roster(
            cls,
            team: Team,
            piece_factory: PieceFactory = PieceFactory(),
    ) -> InsertionResult[Team]:
        method = "TeamBuilder.fill_roster"
        try:
            if not team.roster.is_empty:
                return InsertionResult.failure(
                    CannotOverRideRosterException(f"{method}: {CannotOverRideRosterException.DEFAULT_MESSAGE}")
                )
            for order in team.schema.battle_order:
                build_result = piece_factory.build(
                    team=team,
                    name=order.name,
                    rank=order.rank,
                    id_emitter=id_emitter.piece_id,
                    roster_number=order.roster_number,
                    opening_square=order.opening_square_name,
                )
                if build_result.is_failure():
                    return InsertionResult.failure(build_result.exception)
                push_result = team.roster.push_unique_item(build_result.payload)
                if push_result.is_failure():
                    return InsertionResult.failure(push_result.exception)
        except Exception as ex:
            return InsertionResult.failure(
                FillingTeamRosterFailedException(
                    ex=ex, message=f"{method}: {FillingTeamRosterFailedException.DEFAULT_MESSAGE}"
                )
            )