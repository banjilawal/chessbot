# src/domain/metadata/unions/model/player/human/types.py

"""
Module: domain.metadata.unions.player.human.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import HumanPlayerBlueprint, HumanPlayer, PlayerTypeUnion
from transit import HumanPlayerCarrier


class HumanPlayerTypeUnion(PlayerTypeUnion[HumanPlayer]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating a
            HumanPlayer.

    Attributes:
        model: Type[HumanPlayer]
        carrier: Type[HumanPlayerCarrier]
        blueprint: Type[HumanPlayerBlueprint]

    Provides:

    Super Class:
        PlayerTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[HumanPlayer]] | None = None,
            carrier: Optional[Type[HumanPlayerCarrier]] | None = None, 
            blueprint: Optional[Type[HumanPlayerBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[HumanPlayer]]
            carrier: Optional[Type[HumanPlayerCarrier]
            blueprint: Optional[Type[HumanPlayerBlueprint] 
        """
        super().__init__(
            model=model or HumanPlayer,
            carrier=carrier or HumanPlayerCarrier, 
            blueprint=blueprint or HumanPlayerBlueprint
        )
    
    @property
    def model(self) -> Type[HumanPlayer]:
        return cast(Type[HumanPlayer], super().model)
    
    @property
    def carrier(self) -> Type[HumanPlayerCarrier]:
        return cast(Type[HumanPlayerCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[HumanPlayerBlueprint]:
        return cast(Type[HumanPlayerBlueprint], super().blueprint)