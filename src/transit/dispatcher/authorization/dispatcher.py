# src/transit/dispatcher/authorization/dispatcher.py

"""
Module: transit.dispatcher.authorization.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar


from artifcat import Decision
from authorization import Authorizer
from exchange import PermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="PermissionRequest")

class AuthorizationDispatcher(ABC, Generic[T]):
    """
    Role
        -   Permission Authorization Manager

    Responsibilities:
        1.  Grant

    Attributes:
        authorizer: Authorizer[T]

    Provides:
        -   def  execute(self, request: T) -> Decision[T]

    Super Class:
        Dispatcher
    """
    
    _authorizer: Authorizer[T]
    
    def __init__(self, authorizer: Authorizer[T]):
        """
        Args:
            authorizer: Authorizer[T]
        """
        self._authorizer = authorizer
        
    @property
    def authorizer(self) -> Authorizer[T]:
        return self._authorizer
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Decide if an activity can be performed.
        Args:
            request: T
        Returns:
            Decision[T]
        Raises:
            AuthorizationDispatcherException
        """
        pass