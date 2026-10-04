# src/exchange/responder/validation/struct/chart/exchange.py

"""
Module: exchange.responder.validation.struct.chart.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ChartValidationResponse
from exchange import ChartValidationRequest, ValidationResponder
from transit import ChartValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class ChartValidationResponder(
    ValidationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Chart validation Request-Response workflow.

    Attributes:
        dispatcher: ChartValidationDispatcher[T]

    Provides:
        -   def submit(request: ChartValidationRequest[T]) -> ChartValidationResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: ChartValidationDispatcher[T]):
        """
        Args:
            dispatcher: ChartValidationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> ChartValidationDispatcher[T]:
        return cast(ChartValidationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ChartValidationRequest[T]
    ) -> ChartValidationResponse[T]:
        """
        Args:
            request: ChartValidationRequest[T]
        Result:
            ChartValidationResponse[T]
        Raises:
            ChartValidatorExchangeException
        """
        pass