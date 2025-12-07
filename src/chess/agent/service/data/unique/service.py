# src/chess/agent/service/data/unique/service_.py

"""
Module: chess.agent.service.data.unique.entity_service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from typing import Optional, cast

from chess.team import Team
from chess.system import DeletionResult, InsertionResult, UniqueDataService
from chess.agent import Agent, AgentContextService, AgentDataService, AgentService



class UniqueAgentDataService(UniqueDataService[Agent]):
    DEFAULT_NAME = "UniqueAgentDataService"
    _data_service = AgentDataService
    
    def __init__(
            self,
            id: int,
            name: str = DEFAULT_NAME,
            data_service: AgentDataService = AgentDataService()
    ):
        super().__init__(id=id, name=name, data_service=data_service)
        
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
    
    @property
    def current_team(self) -> Optional[Team]:
        return cast(Team, self.data_service.current_item)
    
    def add_agent(self, agent: Agent) -> InsertionResult[Agent]:
        return self.push_unique_item(agent)
    
    def undo_add_agent(self) -> DeletionResult[Agent]:
        return self.data_service.undo_item_push()
    
    # @LoggingLevelRouter.monitor
    # def push_unique_item(self, item: Agent) -> InsertionResult[Agent]:
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
    #         search_result = self._data_service.search(context=context_validation.payload)
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
