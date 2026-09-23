# src/domain/metadata/manifest/model/rank/knight/manifest.py

"""
Module: domain.metadata.manifest.model.rank.knight.manifest
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
        types: KnightTypeUnion
        nulls: KnightNullGroup

     Provides:

     Super Class:
        RankManifest
     """
    
    def __init__(
            self,
            types: Optional[KnightTypeUnion] | None = None,
            nulls: Optional[KnightNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[KnightTypeUnion]
            nulls: Optional[KnightNullGroup]
        """
        super().__init__(
            types=types or KnightTypeUnion(),
            nulls=nulls or KnightNullGroup(),
        )
        
    @property
    def types(self) -> KnightTypeUnion:
        return cast(KnightTypeUnion, super().types)
    
    @property
    def nulls(self) -> KnightNullGroup:
        return cast(KnightNullGroup, super().nulls)