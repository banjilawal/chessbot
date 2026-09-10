# src/domain/metadata/manifest/game/manifest.py

"""
Module: domain.metadata.manifest.game.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Game, GameNullGroup, GameTypeUnion, ObjectManifest


class GameManifest(ObjectManifest[Game]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Game's security lifecycle.

     Attributes:
        type_union: GameTypeUnion
        null_group: GameNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            type_union: Optional[GameTypeUnion] | None = None,
            null_group: Optional[GameNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[GameTypeUnion]
            null_group: Optional[GameNullGroup]
        """
        super().__init__(
            type_union=type_union or GameTypeUnion(),
            null_group=null_group or GameNullGroup(),
        )
        
    @property
    def types(self) -> GameTypeUnion:
        return cast(GameTypeUnion, super().types)
    
    @property
    def nulls(self) -> GameNullGroup:
        return cast(GameNullGroup, super().nulls)