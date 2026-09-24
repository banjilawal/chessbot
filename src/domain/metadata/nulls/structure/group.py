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
from err import StructureCarrierNullException, StructureBlueprintNullException, StructureNullException

T = TypeVar("T", bound="Structure")


class StructureNullGroup(NullExceptionGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Structure's integrity cycle.

    Attributes:
        structure: StructureNullException
        carrier: StructureCarrierNullException
        blueprint: StructureBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            structure: StructureNullException,
            carrier: StructureCarrierNullException,
            blueprint: StructureBlueprintNullException,
    ):
        """
        Args:
            structure: StructureNullException
            carrier: StructureCarrierNullException
            blueprint: StructureBlueprintNullException
        """
        super().__init__(structure=structure, carrier=carrier, blueprint=blueprint)
    
    @property
    def structure(self) -> StructureNullException:
        return cast(StructureNullException, super().structure)
    
    @property
    def carrier(self) -> StructureCarrierNullException:
        return cast(StructureCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> StructureBlueprintNullException:
        return cast(StructureBlueprintNullException, super().blueprint)