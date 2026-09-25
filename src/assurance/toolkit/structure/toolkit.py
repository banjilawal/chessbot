# src/assurance/toolkit/structure/toolkit.py

"""
Module: assurance.toolkit.structure.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from assurance import StructureHelperTable, ValidatorToolkit
from domain import Structure, StructureManifest

T = TypeVar("T", bound="Structure")


class StructureValidatorToolkit(ValidatorToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            helper: StructureHelperTable[T]
            metadata: StructureManifest[T]

    Provides:

    Super Class:
        ValidatorToolkit
    """
    
    def __init__(
            self,
            helper: StructureHelperTable[T],
            metadata: StructureManifest[T],
    ):
        """
            helper: StructureHelperTable[T]
            metadata: StructureManifest[T]
        """
        super().__init__(helper=helper, metadata=metadata)
    
    
    @property
    def attribute(self) -> StructureHelperTable[T]:
        return cast(StructureHelperTable, super().attribute)
    
    @property
    def metadata(self) -> StructureManifest[T]:
        return cast(StructureManifest, super().metadata)