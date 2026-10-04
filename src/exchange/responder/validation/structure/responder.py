# src/exchange/responder/validation/structure/exchange.py

"""
Module: exchange.responder.validation.structure.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import StructureValidationResponse
from domain import Structure
from exchange import StructureValidationRequest, ValidationResponder
from transit import StructureValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Structure")

class StructureValidationResponder(
    ValidationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Structure validation Request-Response workflow.

    Attributes:
        dispatcher: StructureValidationDispatcher[T]

    Provides:
        -   def submit(request: StructureValidationRequest[T]) -> StructureValidationResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: StructureValidationDispatcher[T]):
        """
        Args:
            dispatcher: StructureValidationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> StructureValidationDispatcher[T]:
        return cast(StructureValidationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: StructureValidationRequest[T]
    ) -> StructureValidationResponse[T]:
        """
        Args:
            request: StructureValidationRequest[T]
        Result:
            StructureValidationResponse[T]
        Raises:
            StructureValidatorExchangeException
        """
        pass