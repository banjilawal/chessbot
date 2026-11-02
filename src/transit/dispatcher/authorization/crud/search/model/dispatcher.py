# src/transit/dispatcher/authorization/crud/search/model/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.search.model.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar, cast

from artifcat import SearchDecision
from authorization import SearchPermitter
from exchange import ModelSearchPermissionRequest
from transit import SearchPermissionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="ModelSearchPermissionRequest")

class ModelSearchPermissionDispatcher(
    SearchPermissionDispatcher[T], ABC, Generic[T]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards a ModelSearchPermitter then send the results
            back to clients.

    Attributes:
        permitter: ModelSearchPermitter[T]
        
    Provides:
        -   def execute(candidate: Any) -> SearchDecision

    Super Class:
        SearchPermissionDispatcher
    """
    
    def __init__(self, permitter: ModelSearchPermitter[T]):
        """
        Args:
            permitter: ModelSearchPermitter[T]
        """
        super().__init__(permitter=permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> SearchDecision:
        """
        Make a decision about a ModelSearchRequest.

        Args:
            candidate: Any
        Returns:
            ModelSearchDecision
        Raises:
            ModelSearchPermissionDispatcherException
        """
        pass
    
    
        
        
