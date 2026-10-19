# src/assurance/validator/factory.py

"""
Module: assurance.validator.factory
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from assurance import RootEnvelopeProducer
from domain import Model
from transit import ValidationRouter
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class ValidationFactory(ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            EntityCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable validation module.

    Attributes:
        producer: RootEnvelopeProducer[T]
        router: ValidationRouter[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[Blueprint[T]|T]:
    Super
    """
    _producer: RootEnvelopeProducer[T]
    _router: ValidationRouter[T]
    
    def __init__(
            self, 
            producer: RootEnvelopeProducer[T],
            router: ValidationRouter[T],
    ):
        """
        Args:
            producer: RootEnvelopeProducer[T]
            router: ValidationRouter[T]
        """
        self._producer = producer
        self._router = router
     
    @property
    def producer(self) -> RootEnvelopeProducer[T]:
        return self._producer
        
    @property
    def router(self) -> ValidationRouter[T]:
        return self._router
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            candidate: Any
        Returns:
           ValidationResult[T]
        Raises:
            ValidatorException
        """
        pass
    
    
