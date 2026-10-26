# src/domain/metadata/context/manifest/context/player/manifest.py

"""
Module: domain.metadata.manifest.context.player.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Player, PlayerContextNullGroup, PlayerContextLayer, ContextManifest


class PlayerContextManifest(ContextManifest[Player]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and ContextTypeUnions for the Player security lifecycle.

     Attributes:
        types: PlayerContextTypeUnion
        nulls: PlayerContextNullGroup

     Provides:

     Super Class:
        ContextManifest
     """
    
    def __init__(
            self,
            types: Optional[PlayerContextLayer] | None = None,
            nulls: Optional[PlayerContextNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[PlayerContextTypeUnion]
            nulls: Optional[PlayerContextNullGroup]
        """
        super().__init__(
            types=types or PlayerContextLayer(),
            nulls=nulls or PlayerContextNullGroup(),
        )
        
    @property
    def types(self) -> PlayerContextLayer:
        return cast(PlayerContextLayer, super().types)
    
    @property
    def nulls(self) -> PlayerContextNullGroup:
        return cast(PlayerContextNullGroup, super().nulls)