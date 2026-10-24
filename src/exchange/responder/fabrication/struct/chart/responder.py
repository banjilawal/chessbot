# src/exchange/responder/fabrication/struct/chart/responder.py

"""
Module: exchange.responder.fabrication.struct.chart.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ChartBuildResponse
from exchange import ChartBuildRequest, BuildResponder
from transit import ChartBuildDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class ChartBuildResponder(
    BuildResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Chart build Request-Response workflow.

    Attributes:
        dispatcher: ChartBuildDispatcher[T]

    Provides:
        -   def execute(request: ChartBuildRequest[T]) -> ChartBuildResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: ChartBuildDispatcher[T]):
        """
        Args:
            dispatcher: ChartBuildDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> ChartBuildDispatcher[T]:
        return cast(ChartBuildDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ChartBuildRequest[T]
    ) -> ChartBuildResponse[T]:
        """
        Args:
            request: ChartBuildRequest[T]
        Result:
            ChartBuildResponse[T]
        Raises:
            ChartValidationResponderException
        """
        pass