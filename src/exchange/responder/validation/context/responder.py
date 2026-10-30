# src/exchange/responder/validation/context/responder.py

"""
Module: exchange.responder.validation.context.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from exchange import ContextValidationRequest, ValidationResponder
from util import LoggingLevelRouter

T = TypeVar("T",)

class ContextValidationResponder(
    ValidationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Context validation Request-Response workflow.

    Attributes:
        dispatcher: ContextValidationDispatcher[T]

    Provides:
        -   def execute(request: ContextValidationRequest[T]) -> ContextValidationResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: ContextValidationDispatcher[T]):
        """
        Args:
            dispatcher: ContextValidationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> ContextValidationDispatcher[T]:
        return cast(ContextValidationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ContextValidationRequest[T]
    ) -> ContextValidationResponse[T]:
        """
        Args:
            request: ContextValidationRequest[T]
        Result:
            ContextValidationResponse[T]
        Raises:
            ContextValidationResponderException
        """
        pass