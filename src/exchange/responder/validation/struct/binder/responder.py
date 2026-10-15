# src/exchange/responder/validation/struct/binder/responder.py

"""
Module: exchange.responder.validation.struct.binder.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import BinderValidationResponse
from exchange import BinderValidationRequest, StructValidationResponder
from transit import BinderValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class BinderValidationResponder(
    StructValidationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Binder validation Request-Response workflow.

    Attributes:
        dispatcher: BinderValidationDispatcher[T]

    Provides:
        -   def submit(request: BinderValidationRequest[T]) -> BinderValidationResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: BinderValidationDispatcher[T]):
        """
        Args:
            dispatcher: BinderValidationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> BinderValidationDispatcher[T]:
        return cast(BinderValidationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: BinderValidationRequest[T]
    ) -> BinderValidationResponse[T]:
        """
        Args:
            request: BinderValidationRequest[T]
        Result:
            BinderValidationResponse[T]
        Raises:
            BinderValidatorExchangeException
        """
        pass