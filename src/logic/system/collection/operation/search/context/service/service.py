# src/logic/system/query/service/transaction.py

"""
Module: logic.system.query.service.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from logic.system import (
    BuildTransaction, Context, IntegrityService, LoggingLevelRouter, SearchResult, Service, StackSearchRouter,
    ValidationTransaction
)

C = TypeVar("C", bound="Context")
T = TypeVar("T")

class QueryService(Service[T]):
    """
    Role:
        -   API
        -   Search Micro Service,

    Responsibilities:
        1.  Public facing API for querying datasets of T objects.
        2.  Encapsulates Search and search filter validation in one extendable module.
        3.  Manage Context integrity lifecycle.

    Args:
        id: int
        name: str
        router: SearchRouter[T]
        context_service: IntegrityService[Context[T]]
        
    Provides:
        -   execute(dataset: List[T], query: Context[T]) -> SearchResult[List[T]]
        
    Super Class:
        QueryService
    """
    _router: StackSearchRouter
    _context_service: SquareContextService
    
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
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, dataset: List[T], context: Context[T]) -> SearchResult[List[T]]:
        pass
    