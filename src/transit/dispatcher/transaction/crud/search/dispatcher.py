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
from operation import Searcher
from request import SearchRequest
from transit import CrudDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="SearchRequest")
# R = TypeVar("R", bound="SearchResult")

class SearchDispatcher(CrudDispatcher[SearchResult], ABC, Generic[T]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute requests among workers then send the result to the correct client

    Attributes:
        worker: Searcher[T]

    Provides:
        -   def  execute(self, request: T) -> R

    Super Class:
        CrudDispatcher
    """
    
    def __init__(self, worker: Searcher[T]):
        """
        Args:
            worker: Searcher[T]
        """
        super().__init__(worker=worker)
        
    
        
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> SearchResult:
        """
        Distribute SearchRequests among workers then forward the results.

        Args:
            request: T
        Returns:
            R
        Raises:
            SearchDispatcherException
        """
        pass
