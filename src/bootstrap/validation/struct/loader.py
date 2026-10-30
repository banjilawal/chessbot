# src/bootstrap/validation/struct/loader.py

"""
Module: bootstrap.validation.struct.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import StructLayerToolkit
from bootstrap import ValidationLoader
from domain import Struct
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")

class StructValidationLoader(ValidationLoader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   StructValidationRequest[T]
            -   StructCarrier[T]
            -   T

    Attributes:

    Provides:
        -   def execute(item: Any) -> ValidationResult[T]

    Super Class:
        Loader
    """
    
    def __init__(self, toolkit: StructLayerToolkit[T]):
        """
        Args:
            toolkit: LayerToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> StructLayerToolkit[T]:
        return cast(StructLayerToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, bootstrap: Any) -> ValidationResult[T]:
        """
        Model a safe StructBlueprint from the candidate.
        Args:
            bootstrap: Any
        Returns:
            ValidationResult[T]
        Raises:
            StructValidatorException
        """
        pass