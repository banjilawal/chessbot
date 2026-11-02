# src/transit/dispatcher/authorization/crud/insertion/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.insertion.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar, cast

from artifcat import InsertionDecision
from authorization import InsertionPermitter
from exchange import InsertionPermissionRequest
from transit import CrudPermissionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="InsertionPermissionRequest")

class InsertionPermissionDispatcher(
    CrudPermissionDispatcher[T], ABC, Generic[T]
):
    """
    Role
        -   Authorization Management

    Responsibilities:
        1.  Direct jobs towards an InsertionPermitter then send the results back
            to clients.

    Attributes:
        permitter: InsertionPermitter[T]
        
    Provides:
        -   def execute(candidate: Any) -> InsertionDecision

    Super Class:
        CrudPermissionDispatcher
    """
    
    def __init__(self, permitter: InsertionPermitter[T]):
        """
        Args:
            permitter: InsertionPermitter[T]
        """
        super().__init__(permitter=permitter)


    @property
    def permitter(self) -> InsertionPermitter[T]:
        return cast(InsertionPermitter[T], super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> InsertionDecision:
        """
        Make a decision about an InsertionRequest.

        Args:
            candidate: Any
        Returns:
            InsertionDecision
        Raises:
            InsertionPermissionDispatcherException
        """
        pass
    
    
        
        
