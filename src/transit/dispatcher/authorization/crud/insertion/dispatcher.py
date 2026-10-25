# src/transit/dispatcher/authorization/crud/insertion/account/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.insertion.account.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic

from exchange import PushPermissionRequest
from transit import CrudPermissionDispatcher
from util import LoggingLevelRouter

TypeVar = ("T")

class PushPermissionDispatcher(
    CrudPermissionDispatcher[PushPermissionRequest], ABC, Generic[T]
):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the InsertionBuild workflow.

    Attributes:
        authorizer: InsertionCrudAuthorizer[T]
        
    Provides:
        -   def execute(request: t) -> CrudRequest[InsertionCarrier]

    Super Class:
        PushPermissionDispatcher
    """
    
    def __init__(self, authorizer: Optional[AccountPushAuthorizer] |  None = None):
        """
        Args:
            authorizer: Optional[AccountPushAuthorizer]
        """
        super().__init__(authorizer=authorizer or AccountPushAuthorizer())


    @property
    def authorizer(self) -> AccountPushAuthorizer:
        return cast(AccountPushAuthorizer, super().authorizer)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountPushPermissionRequest) -> Decision:
        """
        Verify a candidate is an EntityCarrier whose payload is safe.
        Args:
            request: AccountPushPermissionRequest
        Returns:
            Decision
        Raises:
            AccountPermissionDispatcherException
        """
        pass
    
    
        
        
