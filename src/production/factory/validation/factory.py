# src/production/factory/validation/factory.py

"""
Module: production.factory.validation.factory
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from production import EnvelopeManager, Factory
from transit import EntityCarrier
from util import LoggingLevelRouter

T = TypeVar("T")

class ValidationFactory(Factory[T], ABC, ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            EntityCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable validation module.

    Attributes:
        manager: EnvelopeManager[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[Blueprint[T]|T]:
    Super
    """
    _manager: EnvelopeManager[T]
    
    def __init__(self, manager: EnvelopeManager[T]):
        """
        Args:
            manager: EnvelopeManager[T]
        """
        self._manager = manager
     
    @property
    def manager(self) -> EnvelopeManager[T]:
        return self._manager
    
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
    
    
