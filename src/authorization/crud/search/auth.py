# src/authorization/crud/search/authorization.py

"""
Module: authorization.crud.search.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import CrudAuthorizer
from domain import SearchRequest
from report import AuthorizationDecision
from toolkit import SearchRequestToolkit
from util import LoggingLevelRouter


T = TypeVar("T", bound="SearchRequest")


class SearchAuthorizer(CrudAuthorizer[T], ABC, Generic[T]):
    """
    Role
        -   Authorization

    Responsibilities:
        1.  Check if an SearchRequest satisfies integrity and consistency requirements.

    Attributes:
         toolkit: SearchRequestToolkit[T]

    Provides:
        -   execute(self, request: T) -> AuthorizationDecision

    Super Class:
        CrudAuthorizer
    """
    
    def __init__(self, toolkit: SearchRequestToolkit[T]):
        """
        Args:
             toolkit: SearchRequestToolkit[T]
        """
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> SearchRequestToolkit[T]:
        return cast(SearchRequestToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AuthorizationDecision:
        """
        Args:
            request: T
        Returns:
            AuthorizationDecision
        Raises:
            SearchAuthorizerException
        """
        pass