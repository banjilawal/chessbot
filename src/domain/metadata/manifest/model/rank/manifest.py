# src/domain/metadata/manifest/model/rank/rank/manifest.py

"""
Module: domain.metadata.manifest.model.rank.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import ModelNullGroup, ModelManifest, Rank, TypeUnion

T = TypeVar("T", bound="Rank")

class RankManifest(ModelManifest[T], Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Rank's security lifecycle.

     Attributes:
        types: RankTypeUnion
        nulls: RankNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: TypeUnion[T],
            nulls: ModelNullGroup[T]
    ):
        """
        Args:
            types: TypeUnion[T],
            nulls: NullExceptionGroup[T]
        """
        super().__init__(types=types, nulls=nulls)