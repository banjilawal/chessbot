# src/chess/agent/service/service.py

"""
Module: chess.agent.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.arena import Arena
from chess.system import BuildResult, EntityService, id_emitter
from chess.agent import Agent, AgentFactory, AgentValidator
from chess.team import Team, TeamSchema, TeamService


class AgentService(EntityService[Agent]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Protects Agent instance's internal state.
    3.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    4.  Single entry point Agent integrity lifecycle management with AgentBuilder and AgentValidator.

    # PARENT
        *   Entity
    
    # PROVIDES:
        *   AgentBuilder
        *   AgentValidator

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    See EntityService class for inherited attributes.
    """
    DEFAULT_NAME = "AgentService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: AgentFactory = AgentFactory(),
            validator: AgentValidator = AgentValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (AgentFactory)
            *   validator (AgentValidator)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def builder(self) -> AgentFactory:
        """get AgentBuilder"""
        return cast(AgentFactory, self.entity_builder)
    
    @property
    def validator(self) -> AgentValidator:
        """get AgentValidator"""
        return cast(AgentValidator, self.entity_validator)
    
    def build_new_team(
            self,
            agent: Agent,
            arena: Arena,
            team_schema: TeamSchema,
            team_service: TeamService = TeamService(),
            arena_service: ArenaService = ArenaService()
    ) -> BuildResult[Team]:
        method = "AgentService.build_new_team"
        try:
            agent_validation = self.validator.validate(candidate=agent)
            if agent_validation.is_failure:
                return BuildResult.failure(agent_validation.exception)
            arena_validation = arena_service.validator.validate(candidate=arena)
            if arena_validation.is_failure:
                return BuildResult.failure(arena_validation.exception)
            
            
            team_build_result = team_service.builder.build(agent=agent, arena=arena, team_schema=team_schema)
            if team
        except Exception as ex:
            return BuildResult.failure(
                AgentServiceBuildingTeamException(
                    ex=ex, message="{method}: {AgentServiceBuildingTeamException.DEFAULT_MESSAGE}"
                )
            )
    
    
    