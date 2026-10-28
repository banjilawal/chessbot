# src/production/factory/validation/model/factory.py

"""
Module: production.factory.validation.model.factory
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import ValidationFactory
from domain import Model
from production import ModelEnvelopeManager
from transit import ModelCarrier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class ModelValidationFactory(ValidationFactory[T], ABC, ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            ModelCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable validation module.

    Attributes:
        manager: ModelEnvelopeManager[T]

    Provides:
        -   def execute(item: Any) -> ValidationResult[ModelCarrier[T]]:
    Super
        ValidationFactory[T]
    """
    
    def __init__(self, manager: ModelEnvelopeManager[T]):
        """
        Args:
            manager: EnvelopeManager[T]
        """
        super().__init__(self=self)
     
    @property
    def manager(self) -> ModelEnvelopeManager[T]:
        return cast(ModelEnvelopeManager[T], super().manager)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[ModelCarrier[T]]:
        """
        Verify the candidate is a ModelCarrier whose payload is safe.
        Args:
            item: Any
        Returns:
           ValidationResult[T]
        Raises:
            ValidatorException
        """
        pass
    
    
