# src/production/resource/producer/context/producer.py

"""
Module: production.resource.producer.context.producer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from bootstrap import ContextValidationLoader
from domain import Context
from production import EnvelopeProducer
from transit import ContextProductEnvelope
from util import LoggingLevelRouter

T = TypeVar("T", bound="Context")

class ContextEnvelopeProducer(EnvelopeProducer[T], ABC, Generic[T]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs safety checks on root (super) class properties.
        2.  Send the ProductEnvelope containing verified super class properties
            and the prime_extract for its client validators.

    Attributes:
        loader: ValidationLoader

    Provides:
        -   def execute(item: Any) -> ValidationResult[ContextProductEnvelope[T]]:

    Super Class:
    """
    _loader: ContextValidationLoader[T]
    
    def __init__(self, loader: ContextValidationLoader[T]):
        """
        Args:
            loader: ContextValidationLoader[T]
        """
        super().__init__(loader=loader)
        
    @property
    def loader(self) -> ContextValidationLoader[T]:
        return cast(ContextValidationLoader[T], super().loader)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[ContextProductEnvelope[T]]:
        pass

    
