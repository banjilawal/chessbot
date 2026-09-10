# src/domain/metadata/manifest/rank/king/manifest.py

"""
Module: domain.metadata.manifest.rank.king.manifest
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
        type_union: KingTypeUnion
        null_group: KingNullGroup

     Provides:

     Super Class:
        RankManifest
     """
    
    def __init__(
            self,
            type_union: Optional[KingTypeUnion] | None = None,
            null_group: Optional[KingNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[KingTypeUnion]
            null_group: Optional[KingNullGroup]
        """
        super().__init__(
            type_union=type_union or KingTypeUnion(),
            null_group=null_group or KingNullGroup(),
        )
        
    @property
    def types(self) -> KingTypeUnion:
        return cast(KingTypeUnion, super().types)
    
    @property
    def nulls(self) -> KingNullGroup:
        return cast(KingNullGroup, super().nulls)