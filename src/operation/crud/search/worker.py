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
from transit import SearchPermissionDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="SearchRequest")
R = TypeVar("R", bound="SearchResult")


class Searcher(CrudWorker[Q, R], ABC, Generic[Q, R]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an SearchRequest

    Attributes:
        permitter: SearchPermissionDispatcher

    Provides:
        -   def execute(request: Q) -> R

    Super Class:
        CrudOperation
    """
    
    def __init__(
            self,
            permitter: SearchPermissionDispatcher,
    ):
        """
        Args:
            permitter: SearchPermissionDispatcher
        """
        super().__init__(permitter=permitter)
    
    
    @property
    def permitter(self) -> SearchPermissionDispatcher:
        return cast(SearchPermissionDispatcher, super().permitter)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> R:
        """
        Args:
            request: Q
        Result:
            R
        Raises:
            SearcherException
        """
        pass