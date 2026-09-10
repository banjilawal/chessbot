# src/domain/metadata/manifest/square/manifest.py

"""
Module: domain.metadata.manifest.square.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Square, SquareNullGroup, SquareTypeUnion, ObjectManifest


class SquareManifest(ObjectManifest[Square]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Square's security lifecycle.

     Attributes:
        type_union: SquareTypeUnion
        null_group: SquareNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            type_union: Optional[SquareTypeUnion] | None = None,
            null_group: Optional[SquareNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[SquareTypeUnion]
            null_group: Optional[SquareNullGroup]
        """
        super().__init__(
            type_union=type_union or SquareTypeUnion(),
            null_group=null_group or SquareNullGroup(),
        )
        
    @property
    def types(self) -> SquareTypeUnion:
        return cast(SquareTypeUnion, super().types)
    
    @property
    def nulls(self) -> SquareNullGroup:
        return cast(SquareNullGroup, super().nulls)