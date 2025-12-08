# src/chess/agent/service/data/service.py

"""
Module: chess.agent.service.data.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import List, cast


from chess.system import DataService, id_emitter
from chess.agent import Agent, AgentContextService, AgentService


class AgentDataService(DataService[Agent]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Stack data structure for Agent objects with no guarantee of uniqueness.
    3.  Implements search, insert, delete, and update operations on Agent objects.
    4.
    5.  Including a AgentCertifier instance creates a microservice for clients.

    # PARENT
        *   DataService

    # PROVIDES:
        *   AgentService
        *   AgentContextService
        *   AgentStack

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    See DataService class for inherited attributes.
    """
    DEFAULT_NAME = "AgentDataService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            items: List[Agent] = List[Agent],
            service: AgentService = AgentService(),
            context_service: AgentContextService = AgentContextService(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   name (str): = DEFAULT_NAME
            *   items (List[Agent]): = List[Agent]
            *   service (AgentService): = AgentService()
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
    def agent_service(self) -> AgentService:
        return cast(AgentService, self.entity_service)
    
    @property
    def agent_context_service(self) -> AgentContextService:
        return cast(AgentContextService, self.context_service)
    

    # @property
    # def data(self) -> AgentService:
    #     return cast(AgentService, self.data)
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
    # def push_item(self, item: Agent) -> InsertionResult[Agent]:
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
    # def search(self, context: AgentContext) -> SearchResult[List[Agent]]:
    #     method = "AgentDataService.finder"
    #     agent_context_service = cast(AgentContextService, self.context_service)
    #
    #     return self.context_service.finder.find(
    #         data_set=self.items,
    #         context=context,
    #         context_validator=self.context_service.item_validator
    #     )
