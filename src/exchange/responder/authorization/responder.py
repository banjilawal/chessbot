# src/exchange/responder/authorization/responder.py

"""
Module: exchange.responder.authorization.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import Decision
from authorization import Permitter
from exchange import PermissionRequest
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
        -   def execute(request: PermissionRequest[T]) -> Decision


    Super Class:
        Responder
    """
    
    _authorizer: Permitter[T]
    _dispatcher: PermissionDispatcher[T]
    
    def __init__(
            self,
            authorizer: Permitter[T],
            dispatcher: PermissionDispatcher[T]
    ):
        """
        Args:
            authorizer: Authorizer[T]
            dispatcher: AuthorizationDispatcher[T]
        """
        self._authorizer = authorizer
        self._dispatcher = dispatcher
        
    @property
    def dispatcher(self) -> PermissionDispatcher[T]:
        return self._authorizer
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PermissionRequest[T]) -> Decision:
        """
        Args:
            request: PermissionRequest[T]
        Result:
            Decision
        Raises:
            AuthorizationResponderException
        """
        pass