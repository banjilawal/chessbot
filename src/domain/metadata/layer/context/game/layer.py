# src/domain/metadata/unions/context/game/types.py

"""
Module: domain.metadata.unions.context.game.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Game, GameContextBlueprint, ContextLayer
from transit import GameContextCarrier


class GameContextLayer(ContextLayer[GameContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Game.

    Attributes:
        model: Type[GameContext]
        carrier: Type[GameContextCarrier]
        blueprint: Type[GameContextBlueprint]

    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[GameContext]] | None = None,
            carrier: Optional[Type[GameContextCarrier]] | None = None,
            blueprint: Optional[Type[GameContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[GameContext]]
            carrier: Optional[Type[GameContextCarrier]
            blueprint: Optional[Type[GameContextBlueprint] 
        """
        super().__init__(
            model=model or GameContext, 
            carrier=carrier or GameContextCarrier, 
            blueprint=blueprint or GameContextBlueprint
        )
    
    @property
    def model(self) -> Type[GameContext]:
        return cast(Type[GameContext], super().model)
    
    @property
    def carrier(self) -> Type[GameContextCarrier]:
        return cast(Type[GameContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[GameContextBlueprint]:
        return cast(Type[GameContextBlueprint], super().contextBlueprint)