# src/transit/dispatcher/authorization/crud/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import Decision
from exchange import CrudPermissionRequest
from transit import AuthorizationDispatcher
from util import LoggingLevelRouter


T = TypeVar("T", bound="CrudPermissionRequest")


class CrudPermissionDispatcher(AuthorizationDispatcher[T], ABC, Generic[T]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the Build workflow.

    Attributes:
        authorizer: CrudAuthorizer[T]

    Provides:
        -   def execute(self, request: T) -> Decision[T]

    Super Class:
        Dispatcher
    """
    _authorizer: CrudAuthorizer[T]
    
    def __init__(self, authorizer: CrudAuthorizer[T]):
        """
        Args:
            authorizer: CrudAuthorizer[T]
        """
        super().__init__(authorizer=authorizer)
        
    @property
    def authorizer(self) -> CrudAuthorizer[T]:
        return cast(CrudAuthorizer[T], super().authorizer)

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Verify a candidate is safe to use.
        Args:
            request: T
        Returns:
            Decision[T]
        Raises:
            CrudPermissionDispatcherException
        """
        pass
