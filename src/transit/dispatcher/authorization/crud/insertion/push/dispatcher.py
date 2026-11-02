# src/transit/dispatcher/authorization/crud/insertion/push/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.insertion.push.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar, cast

from artifcat import PushDecision
from authorization import PushPermitter
from exchange import PushPermissionRequest
from transit import InsertionPermissionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="PushPermissionRequest")

class PushPermissionDispatcher(
    InsertionPermissionDispatcher[T], ABC, Generic[T]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards a PushPermitter then send the results back
            to clients.

    Attributes:
        permitter: PushPermitter[T]
        
    Provides:
        -   def execute(candidate: Any) -> PushDecision

    Super Class:
        InsertionPermissionDispatcher
    """
    
    def __init__(self, permitter:PushPermitter[T]):
        """
        Args:
            permitter: PushPermitter[T]
        """
        super().__init__(permitter=permitter)

    @property
    def permitter(self) -> PushPermitter[T]:
        return cast(PushPermitter[T], super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> PushDecision:
        """
        Make a decision about a PushRequest.

        Args:
            candidate: Any
        Returns:
            PushDecision
        Raises:
            PushPermissionDispatcherException
        """
        pass
    
    
        
        
