# src/exchange/responder/validation/struct/responder.py

"""
Module: exchange.responder.validation.struct.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import StructValidationResponse
from domain import Struct
from exchange import StructValidationRequest, ValidationResponder
from transit import StructValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")

class StructValidationResponder(
    ValidationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Struct validation Request-Response workflow.

    Attributes:
        dispatcher: StructValidationDispatcher[T]

    Provides:
        -   def submit(request: StructValidationRequest[T]) -> StructValidationResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: StructValidationDispatcher[T]):
        """
        Args:
            dispatcher: StructValidationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> StructValidationDispatcher[T]:
        return cast(StructValidationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: StructValidationRequest[T]
    ) -> StructValidationResponse[T]:
        """
        Args:
            request: StructValidationRequest[T]
        Result:
            StructValidationResponse[T]
        Raises:
            StructValidatorExchangeException
        """
        pass