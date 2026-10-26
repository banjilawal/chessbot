# src/domain/metadata/manifest/model/rank/bishop/manifest.py

"""
Module: domain.metadata.manifest.model.rank.bishop.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Bishop, BishopNullWarningSet, BishopLayer, RankManifest


class BishopManifest(RankManifest[Bishop]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Bishop security lifecycle.

     Attributes:
        types: BishopTypeUnion
        nulls: BishopNullGroup

     Provides:

     Super Class:
        RankManifest
     """
    
    def __init__(
            self,
            types: Optional[BishopLayer] | None = None,
            nulls: Optional[BishopNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[BishopTypeUnion]
            nulls: Optional[BishopNullGroup]
        """
        super().__init__(
            types=types or BishopLayer(),
            nulls=nulls or BishopNullWarningSet(),
        )
        
    @property
    def types(self) -> BishopLayer:
        return cast(BishopLayer, super().types)
    
    @property
    def nulls(self) -> BishopNullWarningSet:
        return cast(BishopNullWarningSet, super().nulls)