# src/exchange/responder/validation/structure/register/exchange.py

"""
Module: exchange.responder.validation.structure.register.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import RegisterValidationResponse
from exchange import RegisterValidationRequest, ValidationResponder
from transit import RegisterValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class RegisterValidationResponder(
    ValidationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Register validation Request-Response workflow.

    Attributes:
        dispatcher: RegisterValidationDispatcher[T]

    Provides:
        -   def submit(request: RegisterValidationRequest[T]) -> RegisterValidationResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: RegisterValidationDispatcher[T]):
        """
        Args:
            dispatcher: RegisterValidationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> RegisterValidationDispatcher[T]:
        return cast(RegisterValidationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: RegisterValidationRequest[T]
    ) -> RegisterValidationResponse[T]:
        """
        Args:
            request: RegisterValidationRequest[T]
        Result:
            RegisterValidationResponse[T]
        Raises:
            RegisterValidatorExchangeException
        """
        pass