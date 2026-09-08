# src/domain/metadata/unions/game/types.py

"""
Module: domain.metadata.unions.game.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Game, GameBlueprint, TypeUnion
from transit import GameCarrier


class GameTypeUnion(TypeUnion[Game]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Game.

    Attributes:
        model: Type[Game]
        carrier: Type[GameCarrier]
        blueprint: Type[GameBlueprint]

    Provides:

    Super Class:
        TypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Game]] | None = None,
            carrier: Optional[Type[GameCarrier]] | None = None, 
            blueprint: Optional[Type[GameBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Game]]
            carrier: Optional[Type[GameCarrier]
            blueprint: Optional[Type[GameBlueprint] 
        """
        super().__init__(
            model=model or Game, 
            carrier=carrier or GameCarrier, 
            blueprint=blueprint or GameBlueprint
        )
    
    @property
    def model(self) -> Type[Game]:
        return cast(Type[Game], super().model)
    
    @property
    def carrier(self) -> Type[GameCarrier]:
        return cast(Type[GameCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[GameBlueprint]:
        return cast(Type[GameBlueprint], super().blueprint)