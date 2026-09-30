# src/transit/carrier/model/token/carrier.py

"""
Module: transit.carrier.model.token.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import (
    CombatantTokenBlueprint, KingTokenBlueprint, PawnTokenBlueprint, Token
)
from transit import ModelCarrier

T = TypeVar("T", bound="Token")

class TokenCarrier(ModelCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Token or its Blueprint.

    Attributes:
        is_pawn_token_carrier: bool
        is_king_token_carrier: bool
        is_combatant_token_carrier: bool

    Provides:
        -   def extract_blueprint() -> Optional[TokenBlueprint]

    Super Class:
        ModelCarrier
    """
    
    @property
    def is_king_token_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return isinstance(blueprint, KingTokenBlueprint)
    
    @property
    def is_pawn_token_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return isinstance(blueprint, PawnTokenBlueprint)
    
    @property
    def is_combatant_token_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return (
                not isinstance(blueprint, PawnTokenBlueprint) and
                isinstance(blueprint, CombatantTokenBlueprint)
                
        )


