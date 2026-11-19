# src/microservice/search/microservice.py

"""
Module: microservice.search.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from artifcat import SearchResult
from exchange import SearchRequest
from transit import SearchDispatcher
from util import LoggingLevelRouter

T = TypeVar("T")


class SearchMicroservice(ABC, Generic[T]):
    """
    Role:
        - API
        - Lifecycle Manager
        - Operations Provider
        - Stateless Microservice
        
    About:
        Avoids casting an entity's searchers and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the search-validation security lifecycle.

    Attributes:
        id: int
        controller: Controller[T]
        name: Optional[str]

    Provides:

    Super Class:
        Microservice
    """
    _dispatcher: SearchDispatcher
    
    def __init__(
            self,
            dispatcher: SearchDispatcher
    ):
        """
        Args:
            dispatcher: SearchDispatcher
        """
        self._dispatcher = dispatcher
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: SearchRequest) -> SearchResult:
        pass
    
    
    