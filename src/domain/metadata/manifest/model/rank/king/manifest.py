# src/domain/metadata/manifest/model/rank/king/manifest.py

"""
Module: domain.metadata.manifest.model.rank.king.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import King, KingNullGroup, KingTypeUnion, RankManifest


class KingManifest(RankManifest[King]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an King's security lifecycle.

     Attributes:
        types: KingTypeUnion
        nulls: KingNullGroup

     Provides:

     Super Class:
        RankManifest
     """
    
    def __init__(
            self,
            types: Optional[KingTypeUnion] | None = None,
            nulls: Optional[KingNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[KingTypeUnion]
            nulls: Optional[KingNullGroup]
        """
        super().__init__(
            types=types or KingTypeUnion(),
            nulls=nulls or KingNullGroup(),
        )
        
    @property
    def types(self) -> KingTypeUnion:
        return cast(KingTypeUnion, super().types)
    
    @property
    def nulls(self) -> KingNullGroup:
        return cast(KingNullGroup, super().nulls)