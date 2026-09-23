# src/domain/metadata/manifest/model/rank/rook/manifest.py

"""
Module: domain.metadata.manifest.model.rank.rook.manifest
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
        types: RookTypeUnion
        nulls: RookNullGroup

     Provides:

     Super Class:
        RankManifest
     """
    
    def __init__(
            self,
            types: Optional[RookTypeUnion] | None = None,
            nulls: Optional[RookNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[RookTypeUnion]
            nulls: Optional[RookNullGroup]
        """
        super().__init__(
            types=types or RookTypeUnion(),
            nulls=nulls or RookNullGroup(),
        )
        
    @property
    def types(self) -> RookTypeUnion:
        return cast(RookTypeUnion, super().types)
    
    @property
    def nulls(self) -> RookNullGroup:
        return cast(RookNullGroup, super().nulls)