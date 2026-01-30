# src/chess/owner/service/data/unique/service.py

"""
Module: chess.owner.service.data.unique.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from typing import List, cast

from chess.system import DeletionResult, InsertionResult, SearchResult, Database
from chess.agent import PlayerAgent, AgentContext, AgentContextService, AgentDataService, AgentService


class UniqueAgentDataService(Database[PlayerAgent]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all bag in managed by AgentStackService are unique.
    2.  Guarantee consistency of records in AgentStackService.
    
    # PARENT:
        *   Database

    # PROVIDES:
        *   player_service: -> AgentService
        *   context_service: -> AgentContextService
        *   add_agent: -> InsertionResult[Player]
        *   undo_add_agent: -> DeletionResult[Player]
        *   search_agents: -> SearchResult[List[Player]]

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
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
            *   member_service (AgentStackService): = AgentStackService()

        # RETURNS:
        None

        # RAISES:
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
        return self.data_service.pop()
    
    def search_agents(self, context: AgentContext) -> SearchResult[List[PlayerAgent]]:
        return self.data_service.search(context)
 
    # @LoggingLevelRouter.monitor
    # def push_unique_item(self, item: Player) -> InsertionResult[Player]:
    #     method = "UniqueAgentDataService.push_unique"
    #     try:
    #         validation = self.data.item_validator.validate(item)
    #         if validation.is_failure():
    #             return InsertionResult.failure(validation.exception)
    #
    #         context_validation = self._member_service.context_service.item_builder.build(id=item.id)
    #         if context_validation.is_failure():
    #             return InsertionResult.failure(context_validation.exception)
    #
    #         search_result = self._member_service.search(map=context_validation.payload)
    #         if search_result.is_failure():
    #             return InsertionResult.failure(search_result.exception)
    #
    #         if search_result.is_success():
    #             return InsertionResult.failure(
    #                 AddingDuplicateAgentException(
    #                     f"{method}: {AddingDuplicateAgentException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #         return self._member_service.push_item(item)
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
