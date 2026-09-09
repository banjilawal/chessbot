# src/domain/metadata/manifest/rank/queen/manifest.py

"""
Module: domain.metadata.manifest.rank.queen.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Queen, QueenNullGroup, QueenTypeUnion, RankManifest


class QueenManifest(RankManifest[Queen]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Queen's security lifecycle.

     Attributes:
        type_union: QueenTypeUnion
        null_group: QueenNullGroup

     Provides:

     Super Class:
        RankManifest
     """
    
    def __init__(
            self,
            type_union: Optional[QueenTypeUnion] | None = None,
            null_group: Optional[QueenNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[QueenTypeUnion]
            null_group: Optional[QueenNullGroup]
        """
        super().__init__(
            type_union=type_union or QueenTypeUnion(),
            null_group=null_group or QueenNullGroup(),
        )
        
    @property
    def type_union(self) -> QueenTypeUnion:
        return cast(QueenTypeUnion, super().type_union)
    
    @property
    def null_group(self) -> QueenNullGroup:
        return cast(QueenNullGroup, super().null_group)