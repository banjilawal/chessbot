# src/transit/carrier/model/rank/carrier.py

"""
Module: transit.carrier.model.rank.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Rank
from transit import ModelCarrier


class RankCarrier(ModelCarrier[Rank]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Rank or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Rank|RankBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[RankBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[Rank]
    _blueprint: Optional[RankBlueprint]
    
    def __init__(
            self,
            model: Optional[Rank] | None = None,
            blueprint: Optional[RankBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Rank]
            blueprint: Optional[RankBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Rank | RankBlueprint]:
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
                isinstance(self._blueprint, RankBlueprint)
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
    
    def extract_blueprint(self) -> Optional[RankBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(Type[self._model], self._model)
        return RankBlueprint(
            persona=model.magnitude,
        )
