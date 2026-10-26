# src/domain/metadata/context/manifest/context/game/manifest.py

"""
Module: domain.metadata.manifest.context.game.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Game, GameContextNullGroup, GameContextLayer, ContextManifest


class GameContextManifest(ContextManifest[Game]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and ContextTypeUnions for the Game security lifecycle.

     Attributes:
        types: GameContextTypeUnion
        nulls: GameContextNullGroup

     Provides:

     Super Class:
        ContextManifest
     """
    
    def __init__(
            self,
            types: Optional[GameContextLayer] | None = None,
            nulls: Optional[GameContextNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[GameContextTypeUnion]
            nulls: Optional[GameContextNullGroup]
        """
        super().__init__(
            types=types or GameContextLayer(),
            nulls=nulls or GameContextNullGroup(),
        )
        
    @property
    def types(self) -> GameContextLayer:
        return cast(GameContextLayer, super().types)
    
    @property
    def nulls(self) -> GameContextNullGroup:
        return cast(GameContextNullGroup, super().nulls)