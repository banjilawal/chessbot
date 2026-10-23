# src/exchange/responder/authorization/model/responder.py

"""
Module: exchange.responder.authorization.model.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ModelDecision
from exchange import ModelAuthorizationRequest, AuthorizationResponder
from transit import ModelAuthorizationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class ModelAuthorizationResponder(
    AuthorizationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Model authorization Request-Response workflow.

    Attributes:
        dispatcher: ModelAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: ModelAuthorizationRequest[T]) -> ModelDecision[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: ModelAuthorizationDispatcher[T]):
        """
        Args:
            dispatcher: ModelAuthorizationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> ModelAuthorizationDispatcher[T]:
        return cast(ModelAuthorizationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ModelAuthorizationRequest[T]
    ) -> ModelDecision[T]:
        """
        Args:
            request: ModelAuthorizationRequest[T]
        Result:
            ModelDecision[T]
        Raises:
            ModelAuthorizationResponderException
        """
        pass