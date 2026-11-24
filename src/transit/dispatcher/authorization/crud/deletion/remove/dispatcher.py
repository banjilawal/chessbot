# src/transit/dispatcher/authorization/crud/deletion/remove/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.deletion.remove.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar, cast

from artifcat import RemoveNodeDecision
from authorization import RemoveNodePermitter
from request import RemoveNodePermissionRequest
from transit import DeletionPermissionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="RemoveNodePermissionRequest")

class RemoveNodePermissionDispatcher(
    DeletionPermissionDispatcher[T], ABC, Generic[T]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Distribute jobs between RemoveNodePermitters then send the results back
            to clients.

    Attributes:
        permitter: RemoveNodePermitter[T]
        
    Provides:
        -   def execute(candidate: Any) -> RemoveNodeDecision

    Super Class:
        DeletionPermissionDispatcher
    """
    
    def __init__(self, permitter:RemoveNodePermitter[T]):
        """
        Args:
            permitter: RemoveNodePermitter[T]
        """
        super().__init__(permitter=permitter)

    @property
    def permitter(self) -> RemoveNodePermitter[T]:
        return cast(RemoveNodePermitter[T], super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> RemoveNodeDecision:
        """
        Make a decision about a RemoveRequest.

        Args:
            candidate: Any
        Returns:
            RemoveNodeDecision
        Raises:
            RemoveNodePermissionDispatcherException
        """
        pass
    
    
        
        
