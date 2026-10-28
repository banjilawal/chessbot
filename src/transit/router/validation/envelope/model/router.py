# src/transit/route/validation/envelope/envelope/router.py

"""
Module: transit.route.validation.envelope.model.router
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import LayerToolkit, ModelLayerToolkit
from domain import Model
from transit import ModelCarrier, ProductEnvelope, EnvelopeRouter
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class ModelEnvelopeRouter(EnvelopeRouter[T], ABC, Generic[T]):
    """
    Role
        -   Router
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Use Carrier type to route a ProductEnvelope to a RootEnvelopeConsumer.

    Attributes:
        toolkit: ModelLayerToolkit[T]

    Provides:
        -   def execute(envelope: ProductEnvelope[T]) -> ValidationResult[ModelCarrier[T]]
        
    Super Class:
        EnvelopeRouter
    """
    
    def __init__(self, toolkit: ModelLayerToolkit[T]):
        """
        Args:
            toolkit: ModelLayerToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> ModelLayerToolkit[T]:
        return cast(ModelLayerToolkit[T], super().toolkit)
    
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