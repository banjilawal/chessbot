# src/logic/system/search/service/microservice.py

"""
Module: logic.system.search.service.service
Author: Banji Lawal
Created: 2026-03-31
Version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, TypeVar

from system import (
    Context, IntegrityMicroservice, LoggingLevelRouter, Query, SearchResult, Microservice, SearchRouter
)

T = TypeVar("T")

class SearchMicroservice(ABC, Microservice[T]):
    """
    Role:
        -   API
        -   Lifecycle Manager
        -   Stateless microservice
        -   Operations Provider
        
    The Search Lifecycle:
        1.  Build a Context of the targeted attributes for an entity.
        2.  Build a Query from a collection and the context for processing
            the dataset's members.
        3.  Forward the query to the SearchRouter which produces a SearchResult.

    Responsibilities:
        1.  Search lifecycle owner.
        2.  Baremetal microservice for querying collections.

    Args:
        id: int
        name: str
        router: SearchRouter[T]
        context_service: IntegrityMicroservice[Context[T]]
        
    Provides:
        -   search(context: Query[T]) -> List[SearchResult[T]]
        
    Super Class:
        Microservice
    """
    _router: SearchRouter
    _query_service: IntegrityMicroservice[Query[T]]
    _context_service: IntegrityMicroservice[Context[T]]
    
    def __init__(
            self,
            id: int,
            name: str,
            router: SearchRouter[T],
            query_service: IntegrityMicroservice[Query[T]],
            context_service: IntegrityMicroservice[Context[T]],
    ):
        """
        Args:
            id: int
            name: str
            router: StackSearchRouter[T]
            query_service: IntegrityMicroservice[Query[T]]
            context_service: IntegrityMicroservice[Context[T]]
        """
        super().__init__(id=id, name=name)
        self._router = router
        self._query_service = query_service
        self._context_service = context_service
    
    @property
    @abstractmethod
    def context_service(self) -> IntegrityMicroservice[Context[T]]:
        pass
    
    @property
    @abstractmethod
    def query_service(self) -> IntegrityMicroservice[Query[T]]:
        pass
    
    @property
    @abstractmethod
    def router(self) -> SearchRouter[T]:
        pass
    