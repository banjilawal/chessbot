# src/transit/dispatcher/authorization/crud/search/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.search.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar, cast

from artifcat import SearchDecision
from authorization import SearchPermitter
from exchange import SearchPermissionRequest
from transit import CrudPermissionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="SearchPermissionRequest")

class SearchPermissionDispatcher(
    CrudPermissionDispatcher[T], ABC, Generic[T]
):
    """
    Role
        -   Authorization Management

    Responsibilities:
        1.  Direct jobs towards a SearchPermitter then send the results back
            to clients.

    Attributes:
        permitter: SearchPermitter[T]
        
    Provides:
        -   def execute(candidate: Any) -> SearchDecision

    Super Class:
        CrudPermissionDispatcher
    """
    
    def __init__(self, permitter: SearchPermitter[T]):
        """
        Args:
            permitter: SearchPermitter[T]
        """
        super().__init__(permitter=permitter)


    @property
    def permitter(self) -> SearchPermitter[T]:
        return cast(SearchPermitter[T], super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> SearchDecision:
        """
        Make a decision about a SearchRequest.

        Args:
            candidate: Any
        Returns:
            SearchDecision
        Raises:
            SearchPermissionDispatcherException
        """
        pass
    
    
        
        
