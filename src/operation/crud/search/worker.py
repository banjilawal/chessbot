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
from transit import SearchPermissionDispatcher, SearchRouter
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="SearchRequest")
R = TypeVar("R", bound="SearchResult")


class Searcher(CrudWorker[R, Q], ABC, Generic[R, Q]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an SearchRequest

    Attributes:
        router: SearchRouter[Q]
        dispatcher: SearchPermissionDispatcher

    Provides:
        -   def execute(request: Q) -> R

    Super Class:
        CrudOperation
    """
    
    def __init__(
            self,
            router: SearchRouter[Q],
            dispatcher: SearchPermissionDispatcher,
    ):
        """
        Args:
            router: SearchRouter[Q]
            dispatcher: SearchPermissionDispatcher
        """
        super().__init__(dispatcher=dispatcher)
    
    
    @property
    def dispatcher(self) -> SearchPermissionDispatcher:
        return cast(SearchPermissionDispatcher, super().dispatcher)
    
    
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