# src/transit/carrier/model/token/carrier.py

"""
Module: transit.carrier.model.token.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from domain import (
    Blueprint, CombatantTokenBlueprint, KingTokenBlueprint, PawnTokenBlueprint,
    Token, TokenBlueprint
)
from transit import ModelCarrier

T = TypeVar("T", bound="Token")

class TokenCarrier(ModelCarrier[T], Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Token or its Blueprint.

    Attributes:
        model: Optional[T]
        blueprint: Optional[TokenBlueprint[T]]
        
        is_pawn_token_carrier: bool
        is_king_token_carrier: bool
        is_combatant_token_carrier: bool

    Provides:
        -   def extract_blueprint() -> Optional[TokenBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[T]
    _blueprint: Optional[TokenBlueprint[T]]
    
    def __init__(
            self,
            model: Optional[T] | None = None,
            blueprint: Optional[TokenBlueprint[T]] | None = None,
    ):
        """
        Args:
            model: Optional[T]
            blueprint: Optional[TokenBlueprint[T]]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[T | TokenBlueprint[T]]:
        if self.is_empty:
            return None
        if self.has_model:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None
        )
    
    def extract_blueprint(self) -> Optional[Blueprint[T]]:
        pass
    
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


