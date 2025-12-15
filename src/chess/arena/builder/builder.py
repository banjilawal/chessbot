# src/chess/arena/builder.py

"""
Module: chess.arena.builder
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""

from typing import List, Optional

from chess.agent import Agent, AgentService
from chess.board import BoardService
from chess.game import UniqueGameDataService
from chess.team import Team, TeamService, UniqueTeamDataService
from chess.system import (
    Builder, BuildResult, IdentityService, LoggingLevelRouter, ServiceValidator, ValidationResult,
    id_emitter
)

from chess.arena import (
    Arena, ArenaBuildFailedException, ArenaValidator
)
from chess.team.schema import TeamSchema


class ArenaBuilder(Builder[Arena]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce Arena instances whose integrity is always guaranteed.
    2.  Manage construction of Arena instances that can be used safely by the client.
    3.  Ensure params for Arena creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.
    
    # PARENT:
        *   Builder

    # PROVIDES:
        *   ArenaBuilder

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    def build(
            cls,
            white_agent: Agent,
            black_agent: Agent,
            id: int = id_emitter.arena_id,
            team_service: TeamService = TeamService(),
            agent_service: AgentService = AgentService(),
            board_service: BoardService = BoardService(),
            service_validator: ServiceValidator = ServiceValidator(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[Arena]:
        """
        # ACTION:
        1.  verify arena_variety is a not-null ArenaVariety object.
        2.  Use arena_variety to pick which builder method will create the concrete Arena object.

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   arena_variety (ArenaVariety)
            *   engine_service (Optional[EngineService])

        # Returns:
        ValidationResult[Arena] containing either:
            - On success: Arena in the payload.
            - On failure: Exception.

        # Raises:
            *   ArenaBuildFailedException
        """
        method = "ArenaBuilder.build"
        try:
            # Ensure the id is safe to use.
            id_validation = identity_service.validate_id(candidate=id)
            if id_validation.failure():
                return BuildResult.failure(id_validation.exception)
            
            # Run safety checks on the agents
            for agent in (white_agent, black_agent):
                validation = agent_service.validator.validate(candidate=agent)
                if validation.failure():
                    return BuildResult.failure(validation.exception)
                
            # Handle the case the agents are the same.
            if white_agent == black_agent:
                return BuildResult.failure(
                    ArenaBuildFailedException(f"{method}: The players cannot be the same.")
                )
            
            # build the teams
            team_builds = cls._build_teams(build_params=[(white_agent, TeamSchema.WHITE), (black_agent, TeamSchema.BLACK)], arena=Arena(id=id))
            
            black_team = black_team_build_result.payload
            if black_team != black_agent.current_team:
                black_agent.team_assignments.push_unique_item(black_team)
                
            board_certification = service_validator.validate(board_service)
            if board_certification.failure():
                return BuildResult.failure(board_certification.exception)
    
            return BuildResult.success(
                payload=Arena(
                    id=id,
                    white_team=white_team,
                    black_team=black_team,
                    board=board_service,
                )
            )
      
        # The flow should only get here if the logic did not route all the types of concrete Arenas.
        # In that case wrap the unhandled exception inside an ArenaBuildFailedException then, return
        # the exception chain inside a ValidationResult.
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                ArenaBuildFailedException(
                    ex=ex, message=f"{method}: {ArenaBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_teams(
            cls,
            build_params: List[(Agent, TeamSchema)],
            team_service: TeamService,
            arena: Arena,
    ) -> BuildResult[List[Team]]:
        teams = []
        for build_param in build_params:
            agent, team_schema = build_param
            build_result = team_service.builder.build(agent=agent, team_schema=team_schema, arena=arena)
            if build_result.failure():
                return BuildResult.failure(build_result.exception)
            teams.append(build_result.payload)
        return BuildResult.success(payload=teams)
    