# src/exchange/responder/authorization/struct/binder/responder.py

"""
Module: exchange.responder.authorization.struct.binder.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import BinderDecision
from exchange import BinderAuthorizationRequest, StructAuthorizationResponder
from transit import BinderAuthorizationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class BinderAuthorizationResponder(
    StructAuthorizationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Binder authorization Request-Response workflow.

    Attributes:
        dispatcher: BinderAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: BinderAuthorizationRequest[T]) -> BinderDecision[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: BinderAuthorizationDispatcher[T]):
        """
        Args:
            dispatcher: BinderAuthorizationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> BinderAuthorizationDispatcher[T]:
        return cast(BinderAuthorizationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: BinderAuthorizationRequest[T]
    ) -> BinderDecision[T]:
        """
        Args:
            request: BinderAuthorizationRequest[T]
        Result:
            BinderDecision[T]
        Raises:
            BinderAuthorizationResponderException
        """
        pass