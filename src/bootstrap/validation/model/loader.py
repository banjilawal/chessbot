# src/bootstrap/validation/model/loader.py

"""
Module: bootstrap.validation.context.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import LayerToolkit, ModelLayerToolkit
from bootstrap import ValidationLoader
from domain import Model, ModelPrimeExtract
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class ModelValidationLoader(ValidationLoader[T], ABC, Generic[T]):
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
        -   def execute(item: Any) -> ValidationResult[ModelPrimeExtract[T]

    Super Class:
        ValidationLoader
    """
    
    def __init__(self, toolkit: ModelLayerToolkit[T]):
        """
        Args:
            toolkit: ModelLayerToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> LayerToolkit:
        return cast(ModelLayerToolkit, super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, bootstrap: Any) -> ValidationResult[ModelPrimeExtract[T]]:
        """
        Extract a safe ModelBlueprint from the candidate.
        Args:
            bootstrap: Any
        Returns:
            ValidationResult[ModelBlueprint[T]]
        Raises:
            ModelExtractorException
        """
        pass