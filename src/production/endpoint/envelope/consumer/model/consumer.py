# src/production/endpoint/envelope/consumer/model/consumer.py

"""
Module: production.endpoint.envelope.consumer.model.consumer
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
from production import EnvelopeConsumer
from transit import ModelCarrier, ProductEnvelope
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class ModelEnvelopeConsumer(EnvelopeConsumer[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a subclass instance covered by a ProductEnvelope is safe.

    Attributes:
        toolkit: ModelLayerToolkit[T]

    Provides:
        -   def execute(envelope: ProductEnvelope[T]) -> ValidationResult[ModelCarrier[T]]

    Super Class:
        EnvelopeConsumer
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
        pass