# src/domain/metadata/unions/token/combatant/pawn/types.py

"""
Module: domain.metadata.unions.token.combatant.pawn.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import CombatantTokenUnion, PawnTokenBlueprint, PawnToken
from transit import PawnTokenCarrier


class PawnTokenUnion(CombatantTokenUnion):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a PawnToken.

    Attributes:
        model: Type[PawnToken]
        carrier: Type[PawnTokenCarrier]
        blueprint: Type[PawnTokenBlueprint]

    Provides:

    Super Class:
        ComabtantTokenUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[PawnToken]] | None = None,
            carrier: Optional[Type[PawnTokenCarrier]] | None = None, 
            blueprint: Optional[Type[PawnTokenBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[PawnToken]]
            carrier: Optional[Type[PawnTokenCarrier]]
            blueprint: Optional[Type[PawnTokenBlueprint]]
        """
        super().__init__(
            model=model or PawnToken,
            carrier=carrier or PawnTokenCarrier,
            blueprint=blueprint or PawnTokenBlueprint
        )
    
    @property
    def model(self) -> Type[PawnToken]:
        return cast(Type[PawnToken], super().model)
    
    @property
    def carrier(self) -> Type[PawnTokenCarrier]:
        return cast(Type[PawnTokenCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[PawnTokenBlueprint]:
        return cast(Type[PawnTokenBlueprint], super().blueprint)