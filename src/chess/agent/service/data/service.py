# src/chess/agent/service/data/service.py

"""
Module: chess.agent.service.data.entity_service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import List, cast

from chess.system import DataService, DeletionResult, InsertionResult, LoggingLevelRouter, SearchResult
from chess.agent import (
    Agent, AgentContext, AgentContextService, AgentFactory, AgentService, AgentFinder, AgentDataServiceException,
    AgentValidator
)
from chess.system.data.service.service import D


class AgentDataService(DataService[Agent]):
    DEFAULT_NAME = "AgentDataService"
    
    def __init__(
            self,
            id: int,
            name: str = DEFAULT_NAME,
            items: List[Agent] = List[Agent],
            service: AgentService = AgentService(),
            context_service: AgentContextService = AgentContextService(),
    ):
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
