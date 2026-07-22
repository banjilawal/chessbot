# src/carrier/token/carrier.py

"""
Module: carrier.token.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from blueprint import TokenBlueprint
from carrier import EntityCarrierToggle

from model import Token


class TokenCarrierToggle(EntityCarrierToggle[Token]):
    """
    Role:
        -   ENTITY

    Responsibilities:
        2.  Transports either a Token or its Blueprint.

    Attributes:
        entity: [Token|TokenBlueprint]
        is_empty: bool
        has_overflow: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        to_dict: Dict[str, Any]
        size: int

    Provides:
        -   extract_blueprint() -> Optional[TokenBlueprint]

    Super Class:
        EntityCarrierToggle
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
    def entity(self) -> [Token | TokenBlueprint | None]:
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
    def to_dict(self) -> Dict[str, Any]:
        return {
            "model": self._model,
            "blueprint": self._blueprint
        }

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TokenCarrierToggle):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

