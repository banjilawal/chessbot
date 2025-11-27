# src/chess/team/builder.builder.py

"""
Module: chess.team.builder.builder
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.agent import Agent, AgentService, PushingDuplicateTeamException
from chess.piece import UniquePieceDataService
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter
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
    """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            id: int,
            agent: Agent,
            schema: TeamSchema,
            identity_service: IdentityService = IdentityService(),
            agent_service: AgentService = AgentService(),
            roster: UniquePieceDataService = UniquePieceDataService(),
            hostages: UniquePieceDataService = UniquePieceDataService(),
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
            *   agent_service (AgentService)
            *   schema_validator (TeamSchemaValidator)
        # Returns:
        BuildResult[Team] containing either:
            - On success: Team in the payload.
            - On failure: Exception.
    
        RAISES:
            *   TeamBuildFailedException
        """
        method = "TeamBuilder.builder"
        
        try:
            id_validation = identity_service.validate_id(id)
            if id_validation.is_failure():
                return BuildResult.failure(id_validation.exception)
            
            team_schema_validation = schema_validator.validate(schema)
            if team_schema_validation.is_failure():
                return BuildResult.failure(team_schema_validation.exception)
            
            agent_validation = agent_service.validate_agent(agent)
            if agent_validation.is_failure():
                return BuildResult.failure(agent_validation.exception)
            
            team = Team(id=id, agent=agent, schema=schema, roster=roster, hostages=hostages)
            if team not in agent.team_stack_service.push_team:
                (team)
            
            if team in agent.team_stack_service.find_tean(team) is not None:
                return BuildResult.failure(
                    PushingDuplicateTeamException(
                        f"{method}: {PushingDuplicateTeamException.DEFAULT_MESSAGE}"
                    )
                )
            
            agent.team_stack_service.push_team(team)
            return BuildResult.success(team)
        
        except Exception as ex:
            return BuildResult.failure(
                TeamBuildFailedException(
                    f"{method}: {TeamBuildFailedException.DEFAULT_MESSAGE}",
                    ex
                )
            )
