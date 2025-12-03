# src/chess/agent/service/data/service.py

"""
Module: chess.agent.service.data.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import List, cast

from chess.system import DataService, InsertionResult, LoggingLevelRouter, SearchResult
from chess.agent import (
    Agent, AgentContext, AgentContextService, AgentIntegrityService, AgentSearch, AgentDataServiceException
)


class AgentDataService(DataService[Agent]):
    DEFAULT_NAME = "AgentDataService"
    
    def __init__(
            self,
            id: int,
            name: str = DEFAULT_NAME,
            items: List[Agent] = List[Agent],
            search: AgentSearch = AgentSearch(),
            service: AgentIntegrityService = AgentIntegrityService(),
            context_service: AgentContextService = AgentContextService(),
    ):
        super().__init__(
            id=id,
            name=name,
            items=items,
            search=search,
            service=service,
            context_service=context_service,
        )
        
    @property
    def security_service(self) -> AgentIntegrityService:
        return cast(AgentIntegrityService, self.security_service)
    
    @LoggingLevelRouter.monitor
    def push(self, item: Agent) -> InsertionResult[Agent]:
        method = "AgentDataService.push"
        try:
            validation = self.security_service.item_validator.validate(item)
            if validation.is_failure():
                return InsertionResult.failure(validation.exception)
            self.items.append(item)
            
            return InsertionResult.success(payload=item)
        except Exception as ex:
            return InsertionResult.failure(
                AgentDataServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{AgentDataServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @LoggingLevelRouter.monitor
    def search(self, context: AgentContext) -> SearchResult[List[Agent]]:
        method = "AgentDataService.search"
        return self.search.find(
            data_set=self.items,
            context=context,
            context_validator=self.context_service.item_validator
        )
