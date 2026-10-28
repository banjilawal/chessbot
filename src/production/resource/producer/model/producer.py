# src/production/resource/producer/model/producer.py

"""
Module: production.resource.producer.model.producer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from bootstrap import ModelValidationLoader
from domain import Model
from production import EnvelopeProducer
from transit import ProductEnvelope
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class ModelEnvelopeProducer(EnvelopeProducer[T], ABC, Generic[T]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs safety checks on root (super) class properties.
        2.  Send the ProductEnvelope containing verified super class properties
            and the prime_extract for its client validators.

    Attributes:
        loader: ValidationLoader[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[ProductEnvelope]:

    Super Class:
    """
    _loader: ModelValidationLoader[T]
    
    def __init__(self, loader: ModelValidationLoader[T]):
        """
        Args:
            loader: ModelValidationLoader[T]
        """
        super().__init__(loader=loader)
        
    @property
    def loader(self) -> ModelValidationLoader[T]:
        return cast(ModelValidationLoader[T], super().loader)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[ProductEnvelope[T]]:
        pass

    
