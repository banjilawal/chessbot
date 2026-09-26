# src/exchange/response/validation/model/exchange.py

"""
Module: exchange.response.validation.model.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ModelValidationResponse
from exchange import ModelValidationRequest, ValidatorResponder
from transit import ModelValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class ModelValidationResponder(
    ValidatorResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Model validation Request-Response workflow.

    Attributes:
        dispatcher: ModelValidationDispatcher[T]

    Provides:
        -   def submit(request: ModelValidationRequest[T]) -> ModelValidationResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: ModelValidationDispatcher[T]):
        """
        Args:
            dispatcher: ModelValidationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> ModelValidationDispatcher[T]:
        return cast(ModelValidationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ModelValidationRequest[T]
    ) -> ModelValidationResponse[T]:
        """
        Args:
            request: ModelValidationRequest[T]
        Result:
            ModelValidationResponse[T]
        Raises:
            ModelValidatorExchangeException
        """
        pass