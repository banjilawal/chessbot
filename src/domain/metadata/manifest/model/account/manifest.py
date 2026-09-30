# src/domain/metadata/manifest/model/player/player/manifest.py

"""
Module: domain.metadata.manifest.model.player.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from domain import ModelManifest, Player, PlayerNullGroup, PlayerTypeUnion

T = TypeVar("T", bound="Player")

class PlayerManifest(ModelManifest[T], Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the Player
            security lifecycle.

     Attributes:
        types: PlayerTypeUnion
        nulls: PlayerNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: PlayerTypeUnion[T],
            nulls: PlayerNullGroup[T]
    ):
        """
        Args:
            types: PlayerTypeUnion[T]
            nulls: PlayerNullGroup[T]
        """
        super().__init__(types=types, nulls=nulls)
        
    @property
    def types(self) -> PlayerTypeUnion[T]:
        return cast(PlayerTypeUnion[T], super().types)
    
    @property
    def nulls(self) -> PlayerNullGroup[T]:
        return cast(PlayerNullGroup[T], super().nulls)