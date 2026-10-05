# src/assurance/load/struct/loader.py

"""
Module: assurance.load.struct.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import Loader, StructValidatorToolkit
from domain import Struct, StructPrimeExtract
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")

class StructLoader(Loader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   StructValidationRequest[T]
            -   StructCarrier[T]
            -   StructBlueprint[T]

    Attributes:

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[StructPrimeExtract[T]

    Super Class:
        Loader
    """
    
    def __init__(self, toolkit: StructValidatorToolkit[T]):
        """
        Args:
            toolkit: ValidatorToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> StructValidatorToolkit[T]:
        return cast(StructValidatorToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[StructPrimeExtract[T]]:
        """
        Extract a safe StructBlueprint from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[StructBlueprint[T]]
        Raises:
            StructExtractorException
        """
        pass