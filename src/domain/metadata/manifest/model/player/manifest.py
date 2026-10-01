# src/domain/metadata/manifest/model/player/manifest.py

"""
Module: domain.metadata.manifest.model.player.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Player, PlayerNullGroup, PlayerTypeUnion, ModelManifest


class PlayerManifest(ModelManifest[Player]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Player security lifecycle.

     Attributes:
        types: PlayerTypeUnion
        nulls: PlayerNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[PlayerTypeUnion] | None = None,
            nulls: Optional[PlayerNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[PlayerTypeUnion]
            nulls: Optional[PlayerNullGroup]
        """
        super().__init__(
            types=types or PlayerTypeUnion(),
            nulls=nulls or PlayerNullGroup(),
        )
        
    @property
    def types(self) -> PlayerTypeUnion:
        return cast(PlayerTypeUnion, super().types)
    
    @property
    def nulls(self) -> PlayerNullGroup:
        return cast(PlayerNullGroup, super().nulls)