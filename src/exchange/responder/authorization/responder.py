# src/exchange/responder/authorization/responder.py

"""
Module: exchange.responder.authorization.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import Decision
from transit import PermissionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Decision")

class AuthorizationResponder(ABC, Generic[T]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the authorization Request-Response workflow.

    Attributes:
        dispatcher: AuthorizationDispatcher[T]

    Provides:
        -   def execute(candidate: Any) -> Decision


    Super Class:
        Responder
    """
    
    _dispatcher: PermissionDispatcher[T]
    
    def __init__(
            self,
            dispatcher: PermissionDispatcher[T]
    ):
        """
        Args:
            dispatcher: AuthorizationDispatcher[T]
        """
        self._dispatcher = dispatcher
        
    @property
    def dispatcher(self) -> PermissionDispatcher[T]:
        return self._authorizer
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> Decision:
        """
        Args:
            candidate: Any
        Result:
            Decision
        Raises:
            AuthorizationResponderException
        """
        pass