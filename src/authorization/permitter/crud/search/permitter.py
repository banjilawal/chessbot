# src/authorization/permitter/crud/search/permitter.py

"""
Module: authorization.permitter.crud.search.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import SearchDecision
from authorization import CrudPermitter
from bootstrap import SearchAuthorizationLoader
from exchange import SearchPermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="SearchPermissionRequest")

class SearchPermitter(CrudPermitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a searchDecision about a SearchPermissionRequest then forward
            that searchDecision to a SearchWorker.

    Attributes:
        loader: CrudAuthorizationLoader[T]

    Provides:
        -   def execute(candidate: Any) -> SearchDecision

    Super Class:
        CrudPermitter
    """
    
    def __init__(self, loader: SearchAuthorizationLoader[T]):
        """
        Args:
            loader: SearchAuthorizationLoader[T]
        """
        super().__init__(loader=loader)
    
    @property
    def loader(self) -> SearchAuthorizationLoader[T]:
        return cast(SearchAuthorizationLoader[T], super().loader)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> SearchDecision:
        """
        Grant permission for a search activitu.
        
        Args:
            candidate: Any
        Returns:
           SearchDecision
        Raises:
            SearchPermitterException
        """
        