# src/assurance/loader/structure/loader.py

"""
Module: assurance.loader.structure.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import BlueprintLoader, StructureValidatorToolkit
from domain import Structure, StructureBlueprint
from util import LoggingLevelRouter

T = TypeVar("T", bound="Structure")

class StructureBlueprintLoader(BlueprintLoader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Extract a StructureBlueprint from the validation candidate.

    Attributes:
        toolkit: StructureValidatorToolkit[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[StructureBlueprint[T]]:

    Super Class:
        BlueprintLoader
    """
    
    def __init__(self, toolkit: StructureValidatorToolkit[T]):
        """
        Args:
            toolkit: StructureValidatorToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> StructureValidatorToolkit[T]:
        return cast(StructureValidatorToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[StructureBlueprint[T]]:
        """
        Extract a safe StructureBlueprint from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[StructureBlueprint[T]]
        Raises:
            StructureBlueprintLoaderException
        """
        pass