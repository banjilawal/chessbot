# src/transit/dispatcher/authorization/crud/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, TypeVar, cast

from artifcat import CrudDecision
from authorization import CrudPermitter
from exchange import CrudPermissionRequest
from transit import PermissionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="CrudPermissionRequest")

class CrudPermissionDispatcher(PermissionDispatcher[T]):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards a CrudPermitter then send the results back
            to clients.

    Attributes:
        permitter: CrudPermitter[T]

    Provides:
        -   def  execute(candidate: Any) -> CrudDecision

    Super Class:
        PermissionDispatcher
    """
    
    def __init__(self, permitter: CrudPermitter[T]):
        """
        Args:
             permitter: CrudPermitter[T]
        """
        super().__init__(permitter=permitter)
        
    @property
    def permitter(self) -> CrudPermitter:
        return cast(CrudPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> CrudDecision:
        """
        Make a decision about a CrudRequest.

        Args:
            candidate: Any
        Returns:
            CrudDecision
        Raises:
            CrudPermissionDispatcherException
        """
        pass