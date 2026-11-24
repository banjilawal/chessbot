# src/transit/dispatcher/authorization/crud/insertion/add/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.insertion.add.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar, cast

from artifcat import AddNodeDecision
from authorization import AddNodePermitter
from request import AddNodePermissionRequest
from transit import InsertionPermissionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="AddNodePermissionRequest")

class AddNodePermissionDispatcher(
    InsertionPermissionDispatcher[T], ABC, Generic[T]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Distribute jobs between AddNodePermitters then send the results back
            to clients.

    Attributes:
        permitter: AddNodePermitter[T]
        
    Provides:
        -   def execute(candidate: Any) -> AddNodeDecision

    Super Class:
        InsertionPermissionDispatcher
    """
    
    def __init__(self, permitter:AddNodePermitter[T]):
        """
        Args:
            permitter: AddNodePermitter[T]
        """
        super().__init__(permitter=permitter)

    @property
    def permitter(self) -> AddNodePermitter[T]:
        return cast(AddNodePermitter[T], super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AddNodeDecision:
        """
        Make a decision about a AddRequest.

        Args:
            candidate: Any
        Returns:
            AddNodeDecision
        Raises:
            AddNodePermissionDispatcherException
        """
        pass
    
    
        
        
