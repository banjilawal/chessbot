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
from exchange import Responder, AuthorizationRequest
from transit import AuthorizationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class AuthorizationResponder(Responder[AuthorizationResult], ABC, Generic[T]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the authorization Request-Response workflow.

    Attributes:
        dispatcher: AuthorizationDispatcher[T]

    Provides:
        -   def submit(request: AuthorizationRequest[T]) -> Decision[T]


    Super Class:
        Responder
    """
    
    def __init__(self, dispatcher: AuthorizationDispatcher[T]):
        """
        Args:
            dispatcher: AuthorizationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> AuthorizationDispatcher[T]:
        return cast(AuthorizationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest[T]) -> Decision[T]:
        """
        Args:
            request: AuthorizationRequest[T]
        Result:
            Decision[T]
        Raises:
            AuthorizationResponderException
        """
        pass