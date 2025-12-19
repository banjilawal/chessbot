# src/chess/agent/service/data/service.py

"""
Module: chess.agent.service.data.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import List, cast


from chess.system import DataService, id_emitter
from chess.agent import PlayerAgent, AgentContextService, PlayerAgentService


class AgentDataService(DataService[PlayerAgent]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Microservice API for managing and searching PlayerAgent collections.
    2.  Assures collection is always reliable.
    3.  Assure only valid Agents are put in the collection.
    4.  Assure updates do not break the integrity individual items in the collection or
        the collection itself.
    5.  Provide PlayerAgent stack data structure with no guarantee of uniqueness.
    6.  Search utility.
    
    # PARENT:
        *   DataService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DataService class for inherited attributes.
    """
    SERVICE_NAME = "AgentDataService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[PlayerAgent] = List[PlayerAgent],
            service: PlayerAgentService = PlayerAgentService(),
            context_service: AgentContextService = AgentContextService(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   designation (str): = SERVICE_NAME
            *   items (List[PlayerAgent]): = List[PlayerAgent]
            *   service (PlayerAgentService): = PlayerAgentService()
            *   context_service (AgentContextService): = AgentContextService()

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
        
    @property
    def agent_service(self) -> PlayerAgentService:
        return cast(PlayerAgentService, self.entity_service)
    
    @property
    def agent_context_service(self) -> AgentContextService:
        return cast(AgentContextService, self.context_service)
    

    # @property
    # def data(self) -> PlayerAgentService:
    #     return cast(PlayerAgentService, self.data)
    #
    # @property
    # def builder(self) -> AgentFactory:
    #     return cast(AgentFactory, self.service.item_builder)
    #
    # @property
    # def validator(self) -> AgentValidator:
    #     return cast(AgentValidator, self.service.item_validator)
    #
    # @property
    # def context_service(self) -> AgentContextService:
    #     return cast(AgentContextService, self.context_service)
    #
    # @LoggingLevelRouter.monitor
    # def push_item(self, item: PlayerAgent) -> InsertionResult[PlayerAgent]:
    #     method = "AgentDataService.push"
    #     try:
    #         validation = self.data.item_validator.validate(item)
    #         if validation.is_failure():
    #             return InsertionResult.failure(validation.exception)
    #         self.items.append(item)
    #
    #         return InsertionResult.success(payload=item)
    #     except Exception as ex:
    #         return InsertionResult.failure(
    #             AgentDataServiceException(ex=ex, message=f"{method}: {AgentDataServiceException.DEFAULT_MESSAGE}")
    #         )
    #
    # @LoggingLevelRouter.monitor
    # def search(self, context: AgentContext) -> SearchResult[List[PlayerAgent]]:
    #     method = "AgentDataService.finder"
    #     agent_context_service = cast(AgentContextService, self.context_service)
    #
    #     return self.context_service.finder.find(
    #         dataset=self.items,
    #         context=context,
    #         context_validator=self.context_service.item_validator
    #     )
