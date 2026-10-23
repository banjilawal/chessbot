# src/exchange/responder/authorization/struct/chart/responder.py

"""
Module: exchange.responder.authorization.struct.chart.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ChartDecision
from exchange import ChartAuthorizationRequest, AuthorizationResponder
from transit import ChartAuthorizationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class ChartAuthorizationResponder(
    AuthorizationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Chart authorization Request-Response workflow.

    Attributes:
        dispatcher: ChartAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: ChartAuthorizationRequest[T]) -> ChartDecision[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: ChartAuthorizationDispatcher[T]):
        """
        Args:
            dispatcher: ChartAuthorizationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> ChartAuthorizationDispatcher[T]:
        return cast(ChartAuthorizationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ChartAuthorizationRequest[T]
    ) -> ChartDecision[T]:
        """
        Args:
            request: ChartAuthorizationRequest[T]
        Result:
            ChartDecision[T]
        Raises:
            ChartAuthorizationResponderException
        """
        pass