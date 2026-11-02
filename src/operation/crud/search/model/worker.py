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
from operation import Searcher
from transit import ModelSearchPermissionDispatcher, SearchPermissionDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="ModelSearchRequest")
R = TypeVar("R", bound="SearchResult")


class ModelSearcher(Searcher[R, Q], ABC, Generic[R, Q]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a ModelSearchRequest

    Attributes:
        dispatcher: SearchPermissionDispatcher

    Provides:
        -   def execute(request: Q) -> R

    Super Class:
        Searcher
    """
    
    def __init__(self, dispatcher: ModelSearchPermissionDispatcher):
        """
        Args:
            dispatcher: SearchPermissionDispatcher
        """
        super().__init__(dispatcher=dispatcher)
    
    
    @property
    def dispatcher(self) -> ModelSearchPermissionDispatcher:
        return cast(ModelSearchPermissionDispatcher, super().dispatcher)
    
    
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