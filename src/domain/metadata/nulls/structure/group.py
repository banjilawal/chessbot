# src/domain/metadata/nulls/structure/group.py

"""
Module: domain.metadata.nulls.structure.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Structure, NullExceptionGroup
from err import BlueprintNullException, StructureNullException

T = TypeVar("T", bound="Structure")

class StructureNullGroup(NullExceptionGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Structure's integrity cycle.

    Attributes:
        structure: StructureNullException
        blueprint: BlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """

    
    def __init__(
            self,
            structure: StructureNullException,
            blueprint: BlueprintNullException,
    ):
        """
        Args:
            structure: StructureNullException
            blueprint: BlueprintNullException
        """
        super().__init__(structure=structure)
        self._blueprint = blueprint
        
    @property
    def structure(self) -> StructureNullException:
        return cast(StructureNullException, super().model)
    
    @property
    def model(self) -> StructureNullException:
        return self.structure
    
    @property
    def blueprint(self) -> BlueprintNullException:
        return self._blueprint