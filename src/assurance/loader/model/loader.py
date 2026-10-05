# src/assurance/load/model/loader.py

"""
Module: assurance.load.model.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import Loader, ModelValidatorToolkit
from domain import Model, ModelPrimeExtract
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class ModelLoader(Loader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ModelValidationRequest[T]
            -   ModelCarrier[T]
            -   ModelBlueprint[T]

    Attributes:

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[ModelPrimeExtract[T]

    Super Class:
        Loader
    """
    
    def __init__(self, toolkit: ModelValidatorToolkit[T]):
        """
        Args:
            toolkit: ValidatorToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> ModelValidatorToolkit[T]:
        return cast(ModelValidatorToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ModelPrimeExtract[T]]:
        """
        Extract a safe ModelBlueprint from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ModelBlueprint[T]]
        Raises:
            ModelExtractorException
        """
        pass