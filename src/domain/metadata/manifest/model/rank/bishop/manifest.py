# src/domain/metadata/manifest/model/rank/bishop/manifest.py

"""
Module: domain.metadata.manifest.model.rank.bishop.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Bishop, BishopNullGroup, BishopTypeUnion, RankManifest


class BishopManifest(RankManifest[Bishop]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Bishop's security lifecycle.

     Attributes:
        types: BishopTypeUnion
        nulls: BishopNullGroup

     Provides:

     Super Class:
        RankManifest
     """
    
    def __init__(
            self,
            types: Optional[BishopTypeUnion] | None = None,
            nulls: Optional[BishopNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[BishopTypeUnion]
            nulls: Optional[BishopNullGroup]
        """
        super().__init__(
            types=types or BishopTypeUnion(),
            nulls=nulls or BishopNullGroup(),
        )
        
    @property
    def types(self) -> BishopTypeUnion:
        return cast(BishopTypeUnion, super().types)
    
    @property
    def nulls(self) -> BishopNullGroup:
        return cast(BishopNullGroup, super().nulls)