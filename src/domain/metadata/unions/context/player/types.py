# src/domain/metadata/unions/context/player/types.py

"""
Module: domain.metadata.unions.context.player.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import ContextTypeUnion, Player, PlayerContextBlueprint
from transit import PlayerContextCarrier


class PlayerContextTypeUnion(ContextTypeUnion[PlayerContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Player.

    Attributes:
        model: Type[PlayerContext]
        carrier: Type[PlayerContextCarrier]
        blueprint: Type[PlayerContextBlueprint]

    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[PlayerContext]] | None = None,
            carrier: Optional[Type[PlayerContextCarrier]] | None = None,
            blueprint: Optional[Type[PlayerContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[PlayerContext]]
            carrier: Optional[Type[PlayerContextCarrier]
            blueprint: Optional[Type[PlayerContextBlueprint] 
        """
        super().__init__(
            model=model or PlayerContext, 
            carrier=carrier or PlayerContextCarrier, 
            blueprint=blueprint or PlayerContextBlueprint
        )
    
    @property
    def model(self) -> Type[PlayerContext]:
        return cast(Type[PlayerContext], super().model)
    
    @property
    def carrier(self) -> Type[PlayerContextCarrier]:
        return cast(Type[PlayerContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[PlayerContextBlueprint]:
        return cast(Type[PlayerContextBlueprint], super().contextBlueprint)