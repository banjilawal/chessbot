# src/transit/carrier/context/token/carrier.py

"""
Module: transit.carrier.context.token.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import TokenContext, TokenContextBlueprint
from transit import ContextCarrier


class TokenContextCarrier(ContextCarrier[TokenContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated TokenContext or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [Token|TokenContextBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[TokenContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[TokenContext]
    _blueprint: Optional[TokenContextBlueprint]
    
    def __init__(
            self,
            model: Optional[TokenContext] | None = None,
            blueprint: Optional[TokenContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[TokenContext]
            blueprint: Optional[TokenContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[TokenContext | TokenContextBlueprint]:
        if self.is_empty:
            return None
        if self.has_model:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, TokenContext)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None and
                isinstance(self._blueprint, TokenContextBlueprint)
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_consistent(self) -> bool:
        return self.size > 1
    
    def extract_blueprint(self) -> Optional[TokenContextBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(TokenContext, self._model)
        return TokenContextBlueprint(
            id=model.id,
            name=model.name,
            rank=model.rank,
            team=model.team,
            color=model.color,
            ransom=model.ransom,
            position=model.position,
            formation=model.formation,
            token_type=model.token_type,
            home_square=model.home_square,
        )


