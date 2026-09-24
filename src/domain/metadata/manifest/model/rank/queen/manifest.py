# src/domain/metadata/manifest/model/rank/queen/manifest.py

"""
Module: domain.metadata.manifest.model.rank.queen.manifest
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
         1.  Aggregates NullExceptions and TypeUnions for the Queen security lifecycle.

     Attributes:
        types: QueenTypeUnion
        nulls: QueenNullGroup

     Provides:

     Super Class:
        RankManifest
     """
    
    def __init__(
            self,
            types: Optional[QueenTypeUnion] | None = None,
            nulls: Optional[QueenNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[QueenTypeUnion]
            nulls: Optional[QueenNullGroup]
        """
        super().__init__(
            types=types or QueenTypeUnion(),
            nulls=nulls or QueenNullGroup(),
        )
        
    @property
    def types(self) -> QueenTypeUnion:
        return cast(QueenTypeUnion, super().types)
    
    @property
    def nulls(self) -> QueenNullGroup:
        return cast(QueenNullGroup, super().nulls)