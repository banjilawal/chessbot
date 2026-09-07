# src/domain/metadata/unions/player/human/types.py

"""
Module: domain.metadata.unions.player.human.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import HumanPlayer, PlayerTypeUnion




class HumanTypeUnion(PlayerTypeUnion[HumanPlayer]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a HumanPlayer.

    Attributes:
        model: Type[HumanPlayer]
        carrier: Type[HumanCarrier]
        blueprint: Type[HumanBlueprint]

    Provides:

    Super Class:
        PlayerTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[HumanPlayer]] | None = None,
            carrier: Optional[Type[HumanCarrier]] | None = None, 
            blueprint: Optional[Type[HumanBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[HumanPlayer]]
            carrier: Optional[Type[HumanCarrier]
            blueprint: Optional[Type[HumanBlueprint] 
        """
        super().__init__(
            model=model or HumanPlayer,
            carrier=carrier or HumanCarrier, 
            blueprint=blueprint or HumanBlueprint
        )
    
    @property
    def model(self) -> Type[HumanPlayer]:
        return cast(Type[HumanPlayer], super().model)
    
    @property
    def carrier(self) -> Type[HumanCarrier]:
        return cast(Type[HumanCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[HumanBlueprint]:
        return cast(Type[HumanBlueprint], super().blueprint)