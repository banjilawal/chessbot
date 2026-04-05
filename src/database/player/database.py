# src/database/coord/database.py

"""
Module: database.coord.database
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from typing import List, cast

from system import DeletionResult, InsertionResult, SearchResult, Database
from database.agent import PlayerAgent, AgentContext, AgentContextService, AgentDataService, AgentService

from database.player import Player


class PlayerDatabase(Database[Player]):
    """
    Role:
        _   Frontend
        -   Interface
        -   Data Protection

    Responsibilities:
        1.  Encapsulates StackService.
        2.  Protects data from direct access.

    Attributes:
        id: int
        size: int
        name: str
        iterator: iter
        is_empty: bool
        current_item: Optional[T]
        integrity_service: IntegrityMicroservice[T]

    Provides:
        -   iterator() ->: iter
        -   insert(item: T) -> InsertionResult:
        -   delete_by_id(id: int) -> DeletionResult[T]:
        -   search(context: Context[T]) -> SearchResult[List[T]]
    """
    Role:Unique Data Stack, Search Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Ensure all bag in managed by AgentStackService are unique.
    2.  Guarantee consistency of records in AgentStackService.
    
    Super Class:
        *   Database

    # PROVIDES:
        *   player_service: -> AgentService
        *   context_service: -> PlayerQueryService
        *   add_agent: -> InsertionResult[Player]
        *   undo_add_agent: -> DeletionResult[Player]
        *   search_agents: -> SearchResult[List[Player]]


    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    DEFAULT_NAME = "PlayerDatabase"
    
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
            *   schema (str): = SERVICE_NAME
            *   member_service (AgentStackService): = AgentStackService()

        # RETURNS:
        None

        Raises:
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
        return self.data_service.undo_current_token_positon()
    
    def search_agents(self, context: AgentContext) -> SearchResult[List[PlayerAgent]]:
        return self.data_service.search_service(context)
 
    # @LoggingLevelRouter.monitor
    # def push_unique_item(self, item: Player) -> InsertionResult[Player]:
    #     method = "PlayerDatabase.push_unique"
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
    #                     f"{method}: {AddingDuplicateAgentException.MSG}"
    #                 )
    #             )
    #         return self._member_service.push_item(item)
    #     except Exception as ex:
    #         return InsertionResult.failure(
    #             UniqueAgentDataServiceException(
    #                 ex=ex,
    #                 msg=(
    #                     f"{method}: "
    #                     f"{UniqueAgentDataServiceException.MSG}"
    #                 )
    #             )
    #         )
