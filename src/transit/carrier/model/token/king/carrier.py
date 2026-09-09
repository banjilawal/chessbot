# src/transit/carrier/model/token/king/carrier.py

"""
Module: transit.carrier.model.token.king.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import KingToken, KingTokenBlueprint
from transit import TokenCarrier


class KingTokenCarrier(TokenCarrier[KingToken]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated KingToken or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Token|KingTokenBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[KingTokenBlueprint]

    Super Class:
        ModelCarrier
    """
    
    def __init__(
            self,
            model: Optional[KingToken] | None = None,
            blueprint: Optional[KingTokenBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[KingToken]
            blueprint: Optional[KingTokenBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[KingToken|KingTokenBlueprint]:
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
                isinstance(self._model, KingToken)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, KingTokenBlueprint)
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_over_capacity(self) -> bool:
        return self.size > 1
    
    def extract_blueprint(self) -> Optional[KingTokenBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(KingToken, self._model)
        return KingTokenBlueprint(
            id=model.id,
            team=model.team,
            rank=model.rank,
            check_count=model.check_count,
            formation=model.formation,
            positions=model.positions,
            home_square=model.home_square,
        )


