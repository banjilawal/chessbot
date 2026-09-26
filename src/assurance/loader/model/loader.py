# src/assurance/loader/model/loader.py

"""
Module: assurance.loader.model.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import BlueprintLoader, ModelValidatorToolkit
from domain import Model, ModelBlueprint
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class ModelBlueprintLoader(BlueprintLoader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Extract a ModelBlueprint from the validation candidate.

    Attributes:
        toolkit: ModelValidatorToolkit[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[ModelBlueprint[T]]:

    Super Class:
        BlueprintLoader
    """
    
    def __init__(self, toolkit: ModelValidatorToolkit[T]):
        """
        Args:
            toolkit: ModelValidatorToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> ModelValidatorToolkit[T]:
        return cast(ModelValidatorToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ModelBlueprint[T]]:
        """
        Extract a safe ModelBlueprint from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ModelBlueprint[T]]
        Raises:
            ModelBlueprintLoaderException
        """
        pass