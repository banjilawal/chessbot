# src/assurance/envelope/producer/validator.py

"""
Module: assurance.envelope.producer.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from assurance import Loader, ValidatorToolkit
from domain import Model
from transit import ProductEnvelope
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class RootEnvelopeProducer(ABC, Generic[T]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs safety checks on root (super) class properties.
        2.  Send the ProductEnvelope containing verified super class properties
            and the prime_extract for its client validators.

    Attributes:
        loader: Loader[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[ProductEnvelope]:

    Super Class:
    """
    _loader: Loader[T]
    
    def __init__(self, loader: Loader[T]):
        """
        Args:
            loader: Loader[T]
        """
        self._loader = loader
        
    @property
    def loader(self) -> Loader[T]:
        return self._loader
        
    @property
    def toolkit(self) -> ValidatorToolkit[T]:
        return self.loader.toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ProductEnvelope[T]]:
        pass

    
