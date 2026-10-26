# src/transit/dispatcher/authorization/crud/insertion/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.insertion.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from artifcat import InsertionDecision
from authorization import InsertionPermitter
from exchange import PushPermissionRequest
from transit import CrudPermissionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="PushPermissionRequest")

class PushPermissionDispatcher(
    CrudPermissionDispatcher[T], ABC, Generic[T]
):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the InsertionBuild workflow.

    Attributes:
        authorizer: InsertionPermitter[T]
        
    Provides:
        -   def execute(request: t) -> CrudRequest[InsertionCarrier]

    Super Class:
        PushPermissionDispatcher
    """
    
    def __init__(self, authorizer:InsertionPermitter[T]):
        """
        Args:
            authorizer: InsertionPermitter
        """
        super().__init__(authorizer=authorizer)


    @property
    def authorizer(self) -> InsertionPermitter[T]:
        return cast(InsertionPermitter[T], super().authorizer)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> InsertionDecision:
        """
        Verify a candidate is an EntityCarrier whose payload is safe.
        Args:
            request: T
        Returns:
            InsertionDecision
        Raises:
            PermissionDispatcherException
        """
        pass
    
    
        
        
