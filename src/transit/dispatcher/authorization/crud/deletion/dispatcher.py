# src/transit/dispatcher/authorization/crud/deletion/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.deletion.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar, cast

from artifcat import DeletionDecision
from authorization import DeletionPermitter
from request import DeletionPermissionRequest
from transit import CrudPermissionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="DeletionPermissionRequest")

class DeletionPermissionDispatcher(
    CrudPermissionDispatcher[T], ABC, Generic[T]
):
    """
    Role
        -   Authorization Management

    Responsibilities:
        1.  Direct jobs towards an DeletionPermitters then send the results back
            to clients.

    Attributes:
        permitter: DeletionPermitter[T]
        
    Provides:
        -   def execute(candidate: Any) -> DeletionDecision

    Super Class:
        CrudPermissionDispatcher
    """
    
    def __init__(self, permitter: DeletionPermitter[T]):
        """
        Args:
            permitter: DeletionPermitter[T]
        """
        super().__init__(permitter=permitter)


    @property
    def permitter(self) -> DeletionPermitter[T]:
        return cast(DeletionPermitter[T], super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> DeletionDecision:
        """
        Make a decision about an DeletionRequest.

        Args:
            candidate: Any
        Returns:
            DeletionDecision
        Raises:
            DeletionPermissionDispatcherException
        """
        pass
    
    
        
        
