# src/chess/team/builder.builder.py

"""
Module: chess.team.builder.builder
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.agent import Agent, AgentIntegrityService
from chess.piece import PieceFactory, UniquePieceDataService
from chess.system import Builder, BuildResult, IdentityService, InsertionResult, LoggingLevelRouter, id_emitter
from chess.team import Team, TeamBuildFailedException, TeamSchema, TeamSchemaValidator

class TeamBuilder(Builder[Team]):
    """
    # ROLE: Builder, Data Integrity Guarantor
  
    # RESPONSIBILITIES:
    Produce Team instances whose integrity is always guaranteed. If any attributes do not pass
    their integrity checks, send an exception instead.
  
    # PROVIDES:
    BuildResult[Team] containing either:
        - On success: Team in the payload.
        - On failure: Exception.
  
    # ATTRIBUTES:
    None
    
    # CONSTRUCTOR:
    None
    
    # CLASS METHODS:
        ## build signature
              build(
                    id: int.
                    agent: Agent,
                    schema: TeamSchema,
                    agent_service: AgentIntegrityService = AgentIntegrityService(),
                    identity_service: IdentityService = IdentityService(),
                    roster: UniquePieceDataService = UniquePieceDataService(),
                    hostages: UniquePieceDataService = UniquePieceDataService(),
                    schema_validator: TeamSchemaValidator = TeamSchemaValidator(),
                ) -> BuildResult[Team]:
        For ease of use and cleaner code dependencies are given default values.
    
    # INSTANCE METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            id: int,
            agent: Agent,
            schema: TeamSchema,
            agent_service: AgentIntegrityService = AgentIntegrityService(),
            identity_service: IdentityService = IdentityService(),
            # roster: UniquePieceDataService = UniquePieceDataService(),
            # hostages: UniquePieceDataService = UniquePieceDataService(),
            schema_validator: TeamSchemaValidator = TeamSchemaValidator(),
    ) -> BuildResult[Team]:
        """
        # ACTION:
        1.  Check ID safety with IdentityService.validate_id.
        2.  Check schema correctness with TeamSchemaValidator.validate.
        3.  Check agent safety with PlayAgentService.validate_player.
        4.  If any check fails, return the exception inside a BuildResult.
        5.  When all checks create a new Team object.
        6.  If the team is not in actor's team_assignments use their team_stack to add it.
    
        # PARAMETERS:
            *   id (int)
            *   agent (Agent)
            *   schema (TeamSchema)
            *   identity_service (IdentityService)
            *   agent_service (AgentIntegrityService)
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
            # Start the error detection process.
            id_validation = identity_service.validate_id(id)
            if id_validation.is_failure():
                return BuildResult.failure(id_validation.exception)
            
            team_schema_validation = schema_validator.validate(schema)
            if team_schema_validation.is_failure():
                return BuildResult.failure(team_schema_validation.exception)
            
            agent_validation = agent_service.item_validator.validate(agent)
            if agent_validation.is_failure():
                return BuildResult.failure(agent_validation.exception)
            # If no errors are detected build the Team object.
            team = Team(
                id=id,
                agent=agent,
                schema=schema,
                roster=UniquePieceDataService(),
                hostages=UniquePieceDataService(),
            )
            fill_roster_result = cls._fill_roster(team, piece_factory=PieceFactory())
            if fill_roster_result.is_failure():
                return BuildResult.failure(fill_roster_result.exception)
            # If the team is not in Agent.team_assignments register it.
            if team not in agent.team_assignments:
                agent.team_assignments.push_unique(team)
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
                    opening_square=order.opening_square,
                )
                if build_result.is_failure():
                    return InsertionResult.failure(build_result.exception)
                push_result = team.roster.push_unique(build_result.payload)
                if push_result.is_failure():
                    return InsertionResult.failure(push_result.exception)
        except Exception as ex:
            return InsertionResult.failure(
                FillingTeamRosterFailedException(
                    ex=ex, message=f"{method}: {FillingTeamRosterFailedException.DEFAULT_MESSAGE}"
                )
            )