# src/domain/metadata/manifest/coord/manifest.py

"""
Module: domain.metadata.manifest.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Coord, CoordNullGroup, CoordTypeUnion, ObjectManifest


class CoordManifest(ObjectManifest[Coord]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Coord's security lifecycle.

     Attributes:
        type_union: CoordTypeUnion
        null_group: CoordNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            type_union: Optional[CoordTypeUnion] | None = None,
            null_group: Optional[CoordNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[CoordTypeUnion]
            null_group: Optional[CoordNullGroup]
        """
        super().__init__(
            type_union=type_union or CoordTypeUnion(),
            null_group=null_group or CoordNullGroup(),
        )
        
    @property
    def type_union(self) -> CoordTypeUnion:
        return cast(CoordTypeUnion, super().type_union)
    
    @property
    def null_group(self) -> CoordNullGroup:
        return cast(CoordNullGroup, super().null_group)