# src/transit/carrier/model/rank/carrier.py

"""
Module: transit.carrier.model.rank.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import King, KingBlueprint, Rank
from transit import RankCarrier


class KingCarrier(RankCarrier[King]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated King or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Rank|KingBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[KingBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[King]
    _blueprint: Optional[KingBlueprint]
    
    def __init__(
            self,
            model: Optional[King] | None = None,
            blueprint: Optional[KingBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Rank]
            blueprint: Optional[KingBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Rank|KingBlueprint]:
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
                isinstance(self._model, Rank)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, KingBlueprint)
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
    
    def extract_blueprint(self) -> Optional[KingBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(King, self._model)
        return KingBlueprint(
            persona=model.persona,
        )
