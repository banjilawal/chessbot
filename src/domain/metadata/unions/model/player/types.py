# src/domain/metadata/unions/model/player/types.py

"""
Module: domain.metadata.unions.player.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import ModelTypeUnion, Player, PlayerBlueprint
from transit import PlayerCarrier


class PlayerTypeUnion(ModelTypeUnion[Player]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Player.

    Attributes:
        model: Type[Player]
        carrier: Type[PlayerCarrier]
        blueprint: Type[PlayerBlueprint]

    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Player]] | None = None,
            carrier: Optional[Type[PlayerCarrier]] | None = None, 
            blueprint: Optional[Type[PlayerBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Player]]
            carrier: Optional[Type[PlayerCarrier]
            blueprint: Optional[Type[PlayerBlueprint] 
        """
        super().__init__(
            model=model or Player, 
            carrier=carrier or PlayerCarrier, 
            blueprint=blueprint or PlayerBlueprint
        )
    
    @property
    def model(self) -> Type[Player]:
        return cast(Type[Player], super().model)
    
    @property
    def carrier(self) -> Type[PlayerCarrier]:
        return cast(Type[PlayerCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[PlayerBlueprint]:
        return cast(Type[PlayerBlueprint], super().blueprint)