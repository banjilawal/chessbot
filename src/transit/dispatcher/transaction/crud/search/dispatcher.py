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
        -   Performance Management

    Responsibilities:
        1.  Distribute requests among workers then send the result to the correct client

    Attributes:
        worker: Searcher[Q, R]

    Provides:
        -   def  execute(self, request: Q) -> R

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
        """
        Distribute SearchRequests among workers then forward the results.

        Args:
            request: Q
        Returns:
            R
        Raises:
            SearchDispatcherException
        """
        pass
