# src/domain/metadata/manifest/rank/rook/manifest.py

"""
Module: domain.metadata.manifest.rank.rook.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RankManifest, Rook, RookNullGroup, RookTypeUnion


class RookManifest(RankManifest[Rook]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Rook's security lifecycle.

     Attributes:
        type_union: RookTypeUnion
        null_group: RookNullGroup

     Provides:

     Super Class:
        RankManifest
     """
    
    def __init__(
            self,
            type_union: Optional[RookTypeUnion] | None = None,
            null_group: Optional[RookNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[RookTypeUnion]
            null_group: Optional[RookNullGroup]
        """
        super().__init__(
            type_union=type_union or RookTypeUnion(),
            null_group=null_group or RookNullGroup(),
        )
        
    @property
    def types(self) -> RookTypeUnion:
        return cast(RookTypeUnion, super().types)
    
    @property
    def nulls(self) -> RookNullGroup:
        return cast(RookNullGroup, super().nulls)