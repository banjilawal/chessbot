# src/operation/crud/search/model/worker.py

"""
Module: operation.crud.search.model.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import SearchResult
from exchange import ModelSearchRequest
from operation import Searcher
from transit import SearchPermissionDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="ModelSearchRequest")
R = TypeVar("R", bound="SearchResult")


class ModelSearcher(Searcher[Q, R], ABC, Generic[Q, R]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a ModelSearchRequest

    Attributes:
        permitter: SearchPermissionDispatcher

    Provides:
        -   def execute(request: Q) -> R

    Super Class:
        Searcher
    """
    
    def __init__(self, permitter: SearchPermissionDispatcher):
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
            ModelSearcherException
        """
        pass