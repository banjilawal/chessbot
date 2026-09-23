# src/domain/metadata/unions/token/combatant/types.py

"""
Module: domain.metadata.unions.token.combatant.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import CombatantBlueprint, CombatantToken, TokenTypeUnion
from transit import CombatantCarrier


class CombatantTokenUnion(TokenTypeUnion[CombatantToken]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a CombatantToken.

    Attributes:
        model: Type[CombatantToken]
        carrier: Type[CombatantCarrier]
        blueprint: Type[CombatantBlueprint]

    Provides:

    Super Class:
        TokenTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[CombatantToken]] | None = None,
            carrier: Optional[Type[CombatantCarrier]] | None = None, 
            blueprint: Optional[Type[CombatantBlueprint]] | None = None,
    ):
        """
        Args:
            odel: Optional[Type[CombatantToken]]
            carrier: Optional[Type[CombatantCarrier]]
            blueprint: Optional[Type[CombatantBlueprint]]
        """
        super().__init__(
            model=model or CombatantToken,
            carrier=carrier or CombatantCarrier,
            blueprint=blueprint or CombatantBlueprint
        )
    
    @property
    def model(self) -> Type[CombatantToken]:
        return cast(Type[CombatantToken], super().model)
    
    @property
    def carrier(self) -> Type[CombatantCarrier]:
        return cast(Type[CombatantCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[CombatantBlueprint]:
        return cast(Type[CombatantBlueprint], super().blueprint)