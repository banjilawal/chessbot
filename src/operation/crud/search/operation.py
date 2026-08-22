# src/operation/crud/search/operation.py

"""
Module: operation.crud.search.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import SearchAuthorizer
from domain import SearchRequest
from operation import CrudOperation
from result import SearchResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="SearchRequest")


class Search(CrudOperation[T], ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Process an SearchRequest.

    Attributes:
        authorizer: SearchAuthorizer[T]

    Provides:
        -   def execute(self, request: T) -> SearchionResult

    Super Class:
        CrudOperation
    """
    
    def __init__(self, authorizer: SearchAuthorizer[T]):
        """
        Args:
            authorizer: SearchAuthorizer[T]
        """
        super().__init__(authorizer=authorizer)
    
    @property
    def authorizer(self) -> SearchAuthorizer[T]:
        return cast(SearchAuthorizer[T], super().authorizer)
    
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