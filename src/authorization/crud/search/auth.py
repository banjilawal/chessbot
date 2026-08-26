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

from artifcat import AuthorizationDecision
from authorization import CrudAuthorizer, SearchPermissionUtility
from domain import SearchRequest
from util import LoggingLevelRouter


T = TypeVar("T", bound="SearchRequest")


class SearchAuthorizer(CrudAuthorizer[T], ABC, Generic[T]):
    """
    Role
        -  Authorization

    Responsibilities:
        1.  Check if a SearchRequest satisfies integrity and consistency requirements.

    Attributes:
         utility: SearchPermissionUtility[T]

    Provides:
        -  execute(self, request: T) -> AuthorizationDecision

    Super Class:
        CrudAuthorizer
    """
    
    def __init__(self, utility: SearchPermissionUtility[T]):
        """
        Args:
             utility: SearchPermissionUtility[T]
        """
        super().__init__(utility=utility)
        
    @property
    def utility(self) -> SearchPermissionUtility[T]:
        return cast(SearchPermissionUtility[T], super().utility)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AuthorizationDecision:
        """
        Decide if a SearchRequest satisfies permission requirements.
        Args:
            request: T
        Returns:
            AuthorizationDecision
        Raises:
            SearchAuthorizerException
        """
        pass