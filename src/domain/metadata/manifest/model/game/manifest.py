# src/domain/metadata/manifest/model/game/manifest.py

"""
Module: domain.metadata.manifest.model.game.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Game, GameNullGroup, GameTypeUnion, ModelManifest


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
            types: Optional[GameTypeUnion] | None = None,
            nulls: Optional[GameNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[GameTypeUnion]
            nulls: Optional[GameNullGroup]
        """
        super().__init__(
            types=types or GameTypeUnion(),
            nulls=nulls or GameNullGroup(),
        )
        
    @property
    def types(self) -> GameTypeUnion:
        return cast(GameTypeUnion, super().types)
    
    @property
    def nulls(self) -> GameNullGroup:
        return cast(GameNullGroup, super().nulls)