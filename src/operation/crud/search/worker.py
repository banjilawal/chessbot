# src/operation/crud/search/worker.py

"""
Module: operation.crud.search.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import SearchResult
from exchange import SearchRequest
from operation import CrudWorker
from util import LoggingLevelRouter

T = TypeVar("T", bound="SearchRequest")


class Searcher(CrudWorker[SearchResult], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an SearchRequest

    Attributes:
        permitter: SearchPermissionPermitter[T]

    Provides:
        -   def execute(self, request: T) -> SearchResult

    Super Class:
        CrudOperation
    """
    
    def __init__(self, permitter: PushPermissionPermitter[T]):
        """
        Args:
            permitter: SearchPermissionPermitter[T]
        """
        super().__init__(permitter=permitter[T])
    
    
    @property
    def permitter(self) -> PushPermissionPermitter[T]:
        return cast(PushPermissionPermitter[T], super().permitter)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> SearchResult:
        """
        Args:
            request: T
        Result:
            SearchResult
        Raises:
            SearcherException
        """
        pass