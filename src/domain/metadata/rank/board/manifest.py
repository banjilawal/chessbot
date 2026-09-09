# src/domain/metadata/manifest/bishop/manifest.py

"""
Module: domain.metadata.manifest.bishop.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Bishop, BishopNullGroup, BishopTypeUnion, ObjectManifest


class BishopManifest(ObjectManifest[Bishop]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Bishop's security lifecycle.

     Attributes:
        type_union: BishopTypeUnion
        null_group: BishopNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            type_union: Optional[BishopTypeUnion] | None = None,
            null_group: Optional[BishopNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[BishopTypeUnion]
            null_group: Optional[BishopNullGroup]
        """
        super().__init__(
            type_union=type_union or BishopTypeUnion(),
            null_group=null_group or BishopNullGroup(),
        )
        
    @property
    def type_union(self) -> BishopTypeUnion:
        return cast(BishopTypeUnion, super().type_union)
    
    @property
    def null_group(self) -> BishopNullGroup:
        return cast(BishopNullGroup, super().null_group)