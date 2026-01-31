# src/chess/owner/database/core/stack.py

"""
Module: chess.owner.database.core.stack
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import List, cast


from chess.system import StackService, id_emitter
from chess.agent import PlayerAgent, AgentContextService, AgentService


class AgentStackService(StackService[PlayerAgent]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Microservice API for managing and searching Player collections.
    2.  Assures collection is always reliable.
    3.  Assure only valid Agents are put in the collection.
    4.  Assure updates do not break the integrity individual bag in the collection or
        the collection itself.
    5.  Provide Player stack data structure with no guarantee of uniqueness.
    6.  Search utility.
    
    # PARENT:
        *   StackService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "AgentStackService"
    
    def service(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[PlayerAgent] = List[PlayerAgent],
            service: AgentService = AgentService(),
            context_service: AgentContextService = AgentContextService(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   name (str): = SERVICE_NAME
            *   bag (List[Player]): = List[Player]
            *   service (AgentService): = AgentService()
            *   context_service (AgentContextService): = AgentContextService()

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().service(
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
    # def push_item(self, item: Player) -> InsertionResult[Player]:
    #     method = "AgentStackService.push"
    #     try:
    #         validation = self.data.item_validator.validate(item)
    #         if validation.is_failure():
    #             return InsertionResult.failure(validation.exception)
    #         self.bag.append(item)
    #
    #         return InsertionResult.success(payload=item)
    #     except Exception as ex:
    #         return InsertionResult.failure(
    #             AgentDataServiceException(ex=ex, message=f"{method}: {AgentDataServiceException.DEFAULT_MESSAGE}")
    #         )
    #
    # @LoggingLevelRouter.monitor
    # def search(self, map: AgentContext) -> SearchResult[List[Player]]:
    #     method = "AgentStackService.finder"
    #     agent_context_service = cast(AgentContextService, self.context_service)
    #
    #     return self.context_service.finder.find(
    #         dataset=self.bag,
    #         map=map,
    #         context_validator=self.context_service.item_validator
    #     )
