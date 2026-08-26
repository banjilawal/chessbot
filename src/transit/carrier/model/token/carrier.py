# src/transit/carrier/token/carrier.py

"""
Module: transit.carrier.token.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from fabrication import TokenBlueprint
from transit.model import Token
from transit.carrier import ModelCarrier


class TokenCarrier(ModelCarrier[Token]):
    """
    Role:
        -  Boundary Carrier

    Responsibilities:
        1.  Transport either a hydrated Token or its Blueprint across validation and other
            processing boundaries

    Attributes:
        entity: Token|TokenBlueprint
        is_empty: bool
        has_overflow: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        to_dict: Dict[str, Any]
        size: int

    Provides:
        -  extract_blueprint() -> Optional[TokenBlueprint]

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
        if self.is_not_carrying_anything:
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
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, TokenBlueprint)
        )

    def extract_blueprint(self) -> Optional[TokenBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return TokenBlueprint(
            id=self._model.id,
            team=self._model.team,
            rank=self._model.rank,
            formation=self._model.formation,
            home_square=self._model.home_square,
        )
    
    @property
    def is_not_carrying_anything(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def is_carrying_too_much(self) -> bool:
        return not self.is_not_carrying_anything

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TokenCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

