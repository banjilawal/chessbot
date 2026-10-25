# src/exchange/responder/authorization/struct/register/responder.py

"""
Module: exchange.responder.authorization.struct.register.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import RegisterDecision
from exchange import RegisterPermissionRequest, StructAuthorizationResponder
from transit import RegisterAuthorizationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class RegisterAuthorizationResponder(
    StructAuthorizationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Register authorization Request-Response workflow.

    Attributes:
        dispatcher: RegisterAuthorizationDispatcher[T]

    Provides:
        -   def execute(request: RegisterPermissionRequest[T]) -> RegisterDecision[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: RegisterAuthorizationDispatcher[T]):
        """
        Args:
            dispatcher: RegisterAuthorizationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> RegisterAuthorizationDispatcher[T]:
        return cast(RegisterAuthorizationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: RegisterPermissionRequest[T]
    ) -> RegisterDecision[T]:
        """
        Args:
            request: RegisterPermissionRequest[T]
        Result:
            RegisterDecision[T]
        Raises:
            RegisterAuthorizationResponderException
        """
        pass