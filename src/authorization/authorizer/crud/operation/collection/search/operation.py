# src/operation/collection/search/operation.py

"""
Module: operation.collection.search.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import SearchAuthorizer, SearchRequest
from operation import CrudOperator
from artifcat import SearchResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="StackService")


class CollectionSearch(CrudOperator[SearchResult], ABC, Generic[T]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces a SearchResult.

    Attributes:
        authorizer: SearchAuthorizer[T]
        
    Provides:
        -   def execute(request: SearchRequest[T]) -> SearchResult

    Super Class:
        CollectionOperation
    """
    
    def __init__(self, authorizer: SearchAuthorizer[T]):
        """
        Args:
            authorizer: SearchAuthorizer[T]
        """
        super().__init__(authorizer=authorizer)
        
    @property
    def authorizer(self) -> SearchAuthorizer[T]:
        return cast(SearchAuthorizer[T], super().authorizer)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: SearchRequest) -> SearchResult:
        pass