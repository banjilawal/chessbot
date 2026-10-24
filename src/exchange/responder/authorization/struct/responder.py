# src/exchange/responder/authorization/struct/responder.py

"""
Module: exchange.responder.authorization.struct.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import StructDecision
from domain import Struct
from exchange import StructAuthorizationRequest, AuthorizationResponder
from transit import StructAuthorizationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")

class StructAuthorizationResponder(
    AuthorizationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Struct authorization Request-Response workflow.

    Attributes:
        dispatcher: StructAuthorizationDispatcher[T]

    Provides:
        -   def execute(request: StructAuthorizationRequest[T]) -> StructDecision[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: StructAuthorizationDispatcher[T]):
        """
        Args:
            dispatcher: StructAuthorizationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> StructAuthorizationDispatcher[T]:
        return cast(StructAuthorizationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: StructAuthorizationRequest[T]
    ) -> StructDecision[T]:
        """
        Args:
            request: StructAuthorizationRequest[T]
        Result:
            StructDecision[T]
        Raises:
            StructAuthorizationResponderException
        """
        pass