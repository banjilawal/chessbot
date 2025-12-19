# src/chess/agent/service/service.py

"""
Module: chess.agent.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from logging import Logger
from typing import List, cast

from chess.arena import Arena
from chess.game import Game, GameContext, UniqueGameDataService, UniqueGameDataServiceException
from chess.system import BuildResult, EntityService, LoggingLevelRouter, SearchResult, ServiceValidator, id_emitter
from chess.agent import PlayerAgent, AgentFactory, AgentServiceException, AgentValidator
from chess.team import Team, TeamSchema, TeamService


class PlayerAgentService(EntityService[PlayerAgent]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing PlayerAgent State Machine microservice API.
    2.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    3.  Is authoritative, single source of truth for PlayerAgent state by providing single entry and exit points to PlayerAgent
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
    DEFAULT_NAME = "PlayerAgentService"
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
            *   designation (str)
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
    def find_games_for_agent(
            self,
            agent: PlayerAgent,
            unique_games_service: UniqueGameDataService,
            service_validator: ServiceValidator = ServiceValidator(),
    ) -> SearchResult[List[Game]]:
        try:
            agent_validation = self.validator.validate(candidate=agent)
            if agent_validation.is_failure:
                return SearchResult.failure(agent_validation.exception)
            service_validation = service_validator.validate(candidate=unique_games_service)
            if service_validation.is_failure:
                return SearchResult.failure(service_validation.exception)
            
            return unique_games_service.search_games(context=GameContext(agent=agent))
        except Exception as ex:
            return SearchResult.failure(
                AgentServiceException(ex=ex, message="{method}: {AgentServiceException.DEFAULT_MESSAGE}")
            )
    
    
    