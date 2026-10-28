# src/transit/route/validation/router.py

"""
Module: transit.route.validation.router
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import LayerToolkit
from transit import ModelCarrier, ProductEnvelope, Router
from util import LoggingLevelRouter

T = TypeVar("T", bound="ValidationResult")

class EnvelopeRouter(Router[T], ABC, Generic[T]):
    """
    Role
        -   Router
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Use Carrier type to route a ProductEnvelope to a RootEnvelopeConsumer.

    Attributes:
        toolkit: LayerToolkit[T]

    Provides:
        -   def execute(envelope: ProductEnvelope[T]) -> ValidationResult[ModelCarrier[T]]
        
    Super Class:
        Router
    """
    _toolkit: LayerToolkit[T]
    
    def __init__(self, toolkit: LayerToolkit[T]):
        """
        Args:
            toolkit: LayerToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> LayerToolkit[T]:
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
            ValidationValidationRouterException
        """
        pass