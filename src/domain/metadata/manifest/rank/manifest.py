# src/domain/metadata/manifest/rank/rank/manifest.py

"""
Module: domain.metadata.manifest.rank.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import NullExceptionGroup, ObjectManifest, Rank, TypeUnion

T = TypeVar("T", bound="Rank")

class RankManifest(ObjectManifest[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Rank's security lifecycle.

     Attributes:
        type_union: RankTypeUnion
        null_group: RankNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            type_union: TypeUnion[T],
            null_group: NullExceptionGroup[T]
    ):
        """
        Args:
            type_union: TypeUnion[T],
            null_group: NullExceptionGroup[T]
        """
        super().__init__(type_union=type_union, null_group=null_group)