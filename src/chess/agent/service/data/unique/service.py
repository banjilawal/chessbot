# src/chess/agent/service/data/unique/service.py

"""
Module: chess.agent.service.data.unique.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from typing import List, cast

from chess.system import DeletionResult, InsertionResult, SearchResult, UniqueDataService
from chess.agent import PlayerAgent, AgentContext, AgentContextService, AgentDataService, AgentService


class UniqueAgentDataService(UniqueDataService[PlayerAgent]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all items in managed by AgentDataService are unique.
    2.  Guarantee consistency of records in AgentDataService.
    
    # PARENT:
        *   UniqueDataService

    # PROVIDES:
        *   player_agent_service: -> AgentService
        *   context_service: -> AgentContextService
        *   add_agent: -> InsertionResult[PlayerAgent]
        *   undo_add_agent: -> DeletionResult[PlayerAgent]
        *   search_agents: -> SearchResult[List[PlayerAgent]]

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See UniqueDataService class for inherited attributes.
    """
    DEFAULT_NAME = "UniqueAgentDataService"
    
    def service(
            self,
            id: int,
            name: str = DEFAULT_NAME,
            data_service: AgentDataService = AgentDataService()
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   name (str): = SERVICE_NAME
            *   data_service (AgentDataService): = AgentDataService()

        # Returns:
        None

        # Raises:
        None
        """
        super().service(id=id, name=name, data_service=data_service)
        
    @property
    def agent_service(self) -> AgentService:
        return cast(AgentDataService, self.data_service).agent_service
    
    @property
    def context_service(self) -> AgentContextService:
        return cast(AgentDataService, self.data_service).agent_context_service
    
    @property
    def size(self) -> int:
        return self.data_service.size
    
    @property
    def is_empty(self) -> bool:
        return self.data_service.is_empty
    
    def add_agent(self, agent: PlayerAgent) -> InsertionResult[PlayerAgent]:
        return self.push_unique_item(agent)
    
    def undo_add_agent(self) -> DeletionResult[PlayerAgent]:
        return self.data_service.undo_item_push()
    
    def search_agents(self, context: AgentContext) -> SearchResult[List[PlayerAgent]]:
        return self.data_service.search(context)
 
    # @LoggingLevelRouter.monitor
    # def push_unique_item(self, item: PlayerAgent) -> InsertionResult[PlayerAgent]:
    #     method = "UniqueAgentDataService.push_unique"
    #     try:
    #         validation = self.data.item_validator.validate(item)
    #         if validation.is_failure():
    #             return InsertionResult.failure(validation.exception)
    #
    #         context_validation = self._data_service.context_service.item_builder.build(id=item.id)
    #         if context_validation.is_failure():
    #             return InsertionResult.failure(context_validation.exception)
    #
    #         search_result = self._data_service.search(map=context_validation.payload)
    #         if search_result.is_failure():
    #             return InsertionResult.failure(search_result.exception)
    #
    #         if search_result.is_success():
    #             return InsertionResult.failure(
    #                 AddingDuplicateAgentException(
    #                     f"{method}: {AddingDuplicateAgentException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #         return self._data_service.push_item(item)
    #     except Exception as ex:
    #         return InsertionResult.failure(
    #             UniqueAgentDataServiceException(
    #                 ex=ex,
    #                 message=(
    #                     f"{method}: "
    #                     f"{UniqueAgentDataServiceException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #         )
