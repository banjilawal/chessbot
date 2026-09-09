# src/domain/metadata/manifest/rank/knight/manifest.py

"""
Module: domain.metadata.manifest.rank.knight.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Knight, KnightNullGroup, KnightTypeUnion, RankManifest


class KnightManifest(RankManifest[Knight]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Knight's security lifecycle.

     Attributes:
        type_union: KnightTypeUnion
        null_group: KnightNullGroup

     Provides:

     Super Class:
        RankManifest
     """
    
    def __init__(
            self,
            type_union: Optional[KnightTypeUnion] | None = None,
            null_group: Optional[KnightNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[KnightTypeUnion]
            null_group: Optional[KnightNullGroup]
        """
        super().__init__(
            type_union=type_union or KnightTypeUnion(),
            null_group=null_group or KnightNullGroup(),
        )
        
    @property
    def type_union(self) -> KnightTypeUnion:
        return cast(KnightTypeUnion, super().type_union)
    
    @property
    def null_group(self) -> KnightNullGroup:
        return cast(KnightNullGroup, super().null_group)