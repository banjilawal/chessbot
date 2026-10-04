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
from domain import Struct, StructBlueprint
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")

class StructLoader(Loader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Extract a StructBlueprint from the validation candidate.

    Attributes:
        toolkit: StructValidatorToolkit[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[StructBlueprint[T]]:

    Super Class:
        Extractor
    """
    
    def __init__(self, toolkit: StructValidatorToolkit[T]):
        """
        Args:
            toolkit: StructValidatorToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> StructValidatorToolkit[T]:
        return cast(StructValidatorToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[StructBlueprint[T]]:
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