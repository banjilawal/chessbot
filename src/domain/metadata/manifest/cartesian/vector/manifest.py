# src/domain/metadata/manifest/vector/manifest.py

"""
Module: domain.metadata.manifest.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Vector, VectorNullGroup, VectorTypeUnion, ObjectManifest


class VectorManifest(ObjectManifest[Vector]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Vector's security lifecycle.

     Attributes:
        type_union: VectorTypeUnion
        null_group: VectorNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            type_union: Optional[VectorTypeUnion] | None = None,
            null_group: Optional[VectorNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[VectorTypeUnion]
            null_group: Optional[VectorNullGroup]
        """
        super().__init__(
            type_union=type_union or VectorTypeUnion(),
            null_group=null_group or VectorNullGroup(),
        )
        
    @property
    def type_union(self) -> VectorTypeUnion:
        return cast(VectorTypeUnion, super().type_union)
    
    @property
    def null_group(self) -> VectorNullGroup:
        return cast(VectorNullGroup, super().null_group)