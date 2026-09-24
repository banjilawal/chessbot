# src/domain/metadata/manifest/model/rank/rank/manifest.py

"""
Module: domain.metadata.manifest.model.rank.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from domain import RankNullGroup, ModelManifest, Rank, RankTypeUnion

T = TypeVar("T", bound="Rank")

class RankManifest(ModelManifest[T], Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and RankTypeUnions for the Rank
            security lifecycle.

     Attributes:
        types: RankRankTypeUnion[T]
        nulls: RankNullGroup[T]

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: RankTypeUnion[T],
            nulls: RankNullGroup[T]
    ):
        """
        Args:
            types: RankTypeUnion[T],
            nulls: RankNullGroup[T]
        """
        super().__init__(types=types, nulls=nulls)
        
    @property
    def types(self) -> RankTypeUnion[T]:
        return cast(RankTypeUnion[T], super().types)
    
    @property
    def nulls(self) -> RankNullGroup[T]:
        return cast(RankNullGroup[T], super().nulls)