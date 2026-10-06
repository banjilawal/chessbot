# src/assurance/envelope/consumer.py

"""
Module: assurance.envelope.consumer
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


class EnvelopeConsumer(ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a subclass instance covered by a ProductEnvelope is safe.

    Attributes:
        toolkit: ValidatorToolkit[T]

    Provides:
        -   def execute(envelope: ProductEnvelope[T]) -> ValidationResult[ModelCarrier[T]]

    Super Class:
    """
    _toolkit: ValidatorToolkit[T]
    
    def __init__(self, toolkit: ValidatorToolkit[T]):
        self._toolkit = toolkit
        
    @property
    def toolkit(self) -> ValidatorToolkit:
        return self._toolkit
        

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, envelope: ProductEnvelope[T]) -> ValidationResult[ModelCarrier[T]]:
        pass