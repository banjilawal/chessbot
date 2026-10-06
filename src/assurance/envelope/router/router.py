# src/assurance/envelope/router/envelope/router.py

"""
Module: assurance.envelope.router.router
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import ValidationResult
from assurance import ValidatorToolkit
from domain import Model
from transit import ModelCarrier, ProductEnvelope
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class EnvelopeRouter(ABC, Generic[T]):
    """
    Role
        -   Router
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Use Carrier type to route a ProductEnvelope to a RootEnvelopeConsumer.

    Attributes:
        toolkit: ValidatorToolkit[T]

    Provides:
        -   def execute(
                    envelope: ProductEnvelope[T]
            ) -> ValidationResult[ModelCarrier[T]]
    Super Class:
    """
    _toolkit: ValidatorToolkit[T]
    
    def __init__(self, toolkit: ValidatorToolkit[T]):
        self._toolkit = toolkit
    
    @property
    def toolkit(self) -> ValidatorToolkit[T]:
        return self._toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, envelope: ProductEnvelope[T]) -> ValidationResult[ModelCarrier[T]]:
        """
        Args:
            envelope: ProductEnvelope[T]
        Returns:
            ValidationResult[ModelCarrier[T]]
        Raises:
            ValidationEnvelopeRouterException
        """
        pass