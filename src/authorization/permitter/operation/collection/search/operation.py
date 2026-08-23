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

from authorization import OperationPermitter, SearchPermitter, SearchRequest
from operation import CrudOperator
from result import SearchResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="StackService")


class CollectionSearch(CrudOperator[SearchResult], ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces a SearchResult.

    Attributes:
        permitter: SearchPermitter[T]
        
    Provides:
        -   def execute(request: SearchRequest[T]) -> SearchResult

    Super Class:
        CollectionOperation
    """
    
    def __init__(self, permitter: SearchPermitter[T]):
        """
        Args:
            permitter: SearchPermitter[T]
        """
        super().__init__(permitter=permitter)
        
    @property
    def permitter(self) -> SearchPermitter[T]:
        return cast(SearchPermitter[T], super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: SearchRequest) -> SearchResult:
        pass