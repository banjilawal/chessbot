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
from authorization import Authorizer
from exchange import PermissionRequest
from transit import AuthorizationDispatcher
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
        -   def execute(request: AuthorizationRequest[T]) -> Decision[T]


    Super Class:
        Responder
    """
    
    _authorizer: Authorizer[T]
    _dispatcher: AuthorizationDispatcher[T]
    
    def __init__(
            self,
            authorizer: Authorizer[T],
            dispatcher: AuthorizationDispatcher[T]
    ):
        """
        Args:
            authorizer: Authorizer[T]
            dispatcher: AuthorizationDispatcher[T]
        """
        self._authorizer = authorizer
        self._dispatcher = dispatcher
        
    @property
    def dispatcher(self) -> AuthorizationDispatcher[T]:
        return self._authorizer
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PermissionRequest[T]) -> Decision[T]:
        """
        Args:
            request: AuthorizationRequest[T]
        Result:
            Decision[T]
        Raises:
            AuthorizationResponderException
        """
        pass