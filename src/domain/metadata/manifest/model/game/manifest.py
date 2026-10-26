# src/domain/metadata/manifest/model/game/manifest.py

"""
Module: domain.metadata.manifest.model.game.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Game, GameNullWarningSet, GameLayer, ModelManifest


class GameManifest(ModelManifest[Game]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the Game security lifecycle.

     Attributes:
        types: GameTypeUnion
        nulls: GameNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[GameLayer] | None = None,
            nulls: Optional[GameNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[GameTypeUnion]
            nulls: Optional[GameNullGroup]
        """
        super().__init__(
            types=types or GameLayer(),
            nulls=nulls or GameNullWarningSet(),
        )
        
    @property
    def types(self) -> GameLayer:
        return cast(GameLayer, super().types)
    
    @property
    def nulls(self) -> GameNullWarningSet:
        return cast(GameNullWarningSet, super().nulls)