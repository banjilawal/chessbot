# src/assurance/router/router.py

"""
Module: assurance.router.router
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar


from artifcat import ValidationResult
from domain import Model
from transit import ModelCarrier, ProductEnvelope
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class ValidationIntraRouter(ABC, Generic[T]):
    """
    Role
        -   Router
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Direct a ProductEnvelope towards the correct SubclassRouter.

    Attributes:
        toolkit: ValidatorToolkit[T]

    Provides:
        -   def execute(
                    envelope: ProductEnvelope[T]
            ) -> ValidationResult[ModelCarrier[T]]
    Super Class:
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            envelope: ProductEnvelope[T]
    ) -> ValidationResult[ModelCarrier[T]]:
        """
        Args:
            envelope: ProductEnvelope[T]
        Returns:
            ValidationResult[ModelCarrier[T]]
        Raises:
            ValidationIntraRouterException
        """
        pass