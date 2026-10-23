# src/exchange/responder/fabrication/struct/responder.py

"""
Module: exchange.responder.fabrication.struct.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import StructBuildResponse
from domain import Struct
from exchange import StructBuildRequest, BuildResponder
from transit import StructBuildDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")

class StructBuildResponder(
    BuildResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Struct build Request-Response workflow.

    Attributes:
        dispatcher: StructBuildDispatcher[T]

    Provides:
        -   def submit(request: StructBuildRequest[T]) -> StructBuildResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: StructBuildDispatcher[T]):
        """
        Args:
            dispatcher: StructBuildDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> StructBuildDispatcher[T]:
        return cast(StructBuildDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: StructBuildRequest[T]
    ) -> StructBuildResponse[T]:
        """
        Args:
            request: StructBuildRequest[T]
        Result:
            StructBuildResponse[T]
        Raises:
            StructValidationResponderException
        """
        pass