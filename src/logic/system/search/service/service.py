# src/logic/system/search/service/service.py

"""
Module: logic.system.search.service.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, TypeVar

from logic.system import (
    Context, IntegrityService, LoggingLevelRouter, Query, SearchResult, Service, StackSearchRouter
)

T = TypeVar("T")

class SearchService(ABC, Service[T]):
    """
    Role:
        -   API
        -   Stateless microservice
        -   Operations Provider

    Responsibilities:
        1.  Baremetal microservice for querying collections.

    Args:
        id: int
        name: str
        router: SearchRouter[T]
        context_service: IntegrityService[Context[T]]
        
    Provides:
        -   search(query: Query[T]) -> List[SearchResult[T]]
        
    Super Class:
        Service
    """
    _router: StackSearchRouter
    _context_service: IntegrityService[Context[T]]
    
    def __init__(
            self,
            id: int,
            name: str,
            router: StackSearchRouter[T],
            context_service: IntegrityService[Context[T]],
    ):
        """
        Args:
            id: int
            name: str
            router: StackSearchRouter[T]
            context_service: IntegrityService[Context[T]]
        """
        super().__init__(id=id, name=name)
        self._router = router
        self._context_service = context_service
    
    @property
    @abstractmethod
    def context_service(self) -> IntegrityService[Context[T]]:
        pass
    
    @property
    @abstractmethod
    def router(self) -> StackSearchRouter[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def search(self, query: Query[T]) -> List[SearchResult[T]]:
        pass
    