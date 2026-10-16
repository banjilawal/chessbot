# src/exchange/responder/fabrication/struct/binder/responder.py

"""
Module: exchange.responder.fabrication.struct.binder.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import BinderBuildResponse
from exchange import BinderBuildRequest, StructBuildResponder
from transit import BinderBuildDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class BinderBuildResponder(
    StructBuildResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Binder build Request-Response workflow.

    Attributes:
        dispatcher: BinderBuildDispatcher[T]

    Provides:
        -   def submit(request: BinderBuildRequest[T]) -> BinderBuildResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: BinderBuildDispatcher[T]):
        """
        Args:
            dispatcher: BinderBuildDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> BinderBuildDispatcher[T]:
        return cast(BinderBuildDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: BinderBuildRequest[T]
    ) -> BinderBuildResponse[T]:
        """
        Args:
            request: BinderBuildRequest[T]
        Result:
            BinderBuildResponse[T]
        Raises:
            BinderValidatorExchangeException
        """
        pass