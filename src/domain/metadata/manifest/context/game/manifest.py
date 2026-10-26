# src/domain/metadata/context/manifest/context/game/manifest.py

"""
Module: domain.metadata.manifest.context.game.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Game, GameContextNullWarningSet, GameContextLayer, ContextManifest


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
            nulls: Optional[GameContextNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[GameContextTypeUnion]
            nulls: Optional[GameContextNullGroup]
        """
        super().__init__(
            types=types or GameContextLayer(),
            nulls=nulls or GameContextNullWarningSet(),
        )
        
    @property
    def types(self) -> GameContextLayer:
        return cast(GameContextLayer, super().types)
    
    @property
    def nulls(self) -> GameContextNullWarningSet:
        return cast(GameContextNullWarningSet, super().nulls)