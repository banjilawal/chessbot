# src/transit/dispatcher/crud/search/dispatcher.py

"""
Module: transit.dispatcher.crud.search.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import SearchResult
from exchange import SearchRequest
from operation import Searcher
from transit import CrudDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="SearchRequest")
R = TypeVar("R", bound="SearchResult")

class SearchDispatcher(CrudDispatcher[Q, R], ABC, Generic[Q, R]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Direct jobs towards a worker then forward the results to clients.

    Attributes:
        worker: Searcher[Q, R]

    Provides:

    Super Class:
        CrudDispatcher
    """
    
    def __init__(self, worker: Searcher[Q, R]):
        """
        Args:
            worker: Searcher[Q, R]
        """
        super().__init__(worker=worker)
        
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> R:
        pass
