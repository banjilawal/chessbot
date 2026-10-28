# src/production/manager/validation/manager.py

"""
Module: production.manager.validation.manager
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from production import EnvelopeProducer
from transit import EntityCarrier, EnvelopeRouter
from util import LoggingLevelRouter

T = TypeVar("T")


class EnvelopeManager(ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            EntityCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable validation module.

    Attributes:
        producer: EnvelopeProducer[T]
        router: EnvelopeRouter[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[EntityCarrier[T]]:
    Super
    """
    _producer: EnvelopeProducer[T]
    _router: EnvelopeRouter[T]
    
    def __init__(
            self,
            producer: EnvelopeProducer[T],
            router: EnvelopeRouter[T],
    ):
        """
        Args:
            producer: EnvelopeProducer[T]
            router: ValidationRouter[T]
        """
        super().__init__()
        self._producer = producer
        self._router = router
     
    @property
    def producer(self) -> EnvelopeProducer[T]:
        return self._producer
        
    @property
    def router(self) -> EnvelopeRouter[T]:
        return self._router
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[EntityCarrier[T]]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            item: Any
        Returns:
           ValidationResult[T]
        Raises:
            ValidatorException
        """
        pass
    
    
