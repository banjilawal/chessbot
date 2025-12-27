# src/chess/agent/service/service.py

"""
Module: chess.agent.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from typing import cast

from chess.system import EntityService, LoggingLevelRouter, Result, id_emitter
from chess.agent import AgentServiceException, PlayerAgent, AgentFactory, AgentValidator
from chess.team import Team, TeamService


class AgentService(EntityService[PlayerAgent]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing PlayerAgent microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for PlayerAgent state by providing single entry and exit points to PlayerAgent
        lifecycle.

    # PARENT:
        *   EntityService
    
    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
        *   See EntityService class for inherited attributes.
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
    
    @LoggingLevelRouter.monitor
    def team_is_registered_to_agent(
            self,
            team: Team,
            agent: PlayerAgent,
            team_service: TeamService = TeamService(),
    ) -> Result[(Team, PlayerAgent)]:
        method = "TeamService.team_is_registered_to_agent"
        team_validation = team_service.validator.validate(team)
        if team_validation.is_failure:
            return Result.failure(
                AgentServiceException(
                    message=f"{method}: {AgentServiceException.ERROR_CODE}", ex=team_validation.exception
                )
            )
        agent_validation = self.validator.validate(agent)
        if agent_validation.is_failure:
            return Result.failure(
                AgentServiceException(
                    message=f"{method}: {AgentServiceException.ERROR_CODE}", ex=agent_validation.exception
                )
            )
        if team.owner != agent:
            return Result.failure(
                AgentServiceException(
                    message=f"{method}: {AgentServiceException.ERROR_CODE}",
                    ex=TeamBelongsToDifferentOwnerException(f"{method}")
                )
            )
        search_result = agent.team_assignments.search_teams(team.id)
        if search_result.is_failure:
            return Result.failure(
                AgentServiceException(
                    message=f"{method}: {AgentServiceException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        if search_result.is_empty:
            return Result.empty()
        if search_result.is_success:
            return Result.success((team, agent))

    
    