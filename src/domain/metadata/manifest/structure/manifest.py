# src/domain/metadata/manifest/strcture/manifest.py

"""
Module: domain.metadata.manifest.structure.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import ObjectManifest, Structure, StructureNullGroup, StructureTypeUnion

T = TypeVar("T", bound="Structure")

class StructureManifest(ObjectManifest[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Structure security lifecycle.

     Attributes:
        types: StructureTypeUnion[T]
        nulls: StructureNullGroup[T]

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: StructureTypeUnion[T],
            nulls: StructureNullGroup[T],
    ):
        """
        Args:
            types: StructureTypeUnion[T]
            nulls: StructureNullGroup[T]
        """
        super().__init__(types=types, nulls=nulls,)

        
    @property
    def types(self) -> StructureTypeUnion[T]:
        return cast(StructureTypeUnion[T], super().types)
    
    @property
    def nulls(self) -> StructureNullGroup:
        return cast(StructureNullGroup, super().nulls)