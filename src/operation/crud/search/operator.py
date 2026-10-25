# src/operation/crud/search/operator.py

"""
Module: operation.crud.search.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import SearchPermitter
from domain import SearchRequest
from operation import CrudWorker
from artifcat import SearchResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="SearchRequest")


class Search(CrudWorker[T], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Process an SearchRequest.

    Attributes:
        permitter: SearchPermitter[T]

    Provides:
        -   def execute(self, request: T) -> SearchionResult

    Super Class:
        CrudOperation
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
    def execute(self, request: T) -> SearchResult:
        """
        Args:
            request: T
        Result:
            SearchResult
        Raises:
            SearchException
        """
        pass