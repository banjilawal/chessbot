# src/domain/metadata/unions/model/player/types.py

"""
Module: domain.metadata.unions.player.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Type

from domain import ModelTypeUnion, Player, PlayerBlueprint
from transit import PlayerCarrier

class PlayerTypeUnion(ModelTypeUnion[Player]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Player.

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
            model: Type[Player],
            carrier: Type[PlayerCarrier],
            blueprint: Type[PlayerBlueprint],
    ):
        """
        Args:
            model: Type[Player]
            carrier: Type[PlayerCarrier]
            blueprint: Type[PlayerBlueprint]
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)
    
    @property
    def model(self) -> Type[Player]:
        return cast(Type[Player], super().model)
    
    @property
    def carrier(self) -> Type[PlayerCarrier]:
        return cast(Type[PlayerCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[PlayerBlueprint]:
        return cast(Type[PlayerBlueprint], super().blueprint)