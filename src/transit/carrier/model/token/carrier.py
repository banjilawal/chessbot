# src/transit/carrier/model/mode/token/carrier.py

"""
Module: transit.carrier.model.model.token.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import Token, TokenBlueprint
from transit import ModelCarrier


class TokenCarrier(ModelCarrier[Token]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Token or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Token|TokenBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[TokenBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[Token]
    _blueprint: Optional[TokenBlueprint]
    
    def __init__(
            self,
            model: Optional[Token] | None = None,
            blueprint: Optional[TokenBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Token]
            blueprint: Optional[TokenBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Token | TokenBlueprint]:
        if self.is_empty:
            return None
        if self.is_carrying_model:
            return self._model
        return self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Token)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, TokenBlueprint)
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def over_capacity(self) -> bool:
        return self.size > 1
    
    def extract_blueprint(self) -> Optional[TokenBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        return TokenBlueprint(
            id=self._model.id,
            team=self._model.team,
            rank=self._model.rank,
            formation=self._model.formation,
            home_square=self._model.home_square,
        )

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TokenCarrier):
            return self.entity == other.entity
        return False


