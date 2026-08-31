# src/transit/carrier/context/rank/carrier.py

"""
Module: transit.carrier.context.rank.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Rank
from transit import ContextCarrier


class RankContextCarrier(ContextCarrier[RankContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated RankContext or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Rank|RankContextBlueprint]

    Provides:
        - def extract_ContextBlueprint() -> Optional[RankContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[RankContext]
    _blueprint: Optional[RankContextBlueprint]
    
    def __init__(
            self,
            model: Optional[RankContext] | None = None,
            blueprint: Optional[RankContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[RankContext]
            blueprint: Optional[RankContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Rank | RankContextBlueprint]:
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
    def is_carrying_ContextBlueprint(self) -> bool:
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
    
    def extract_ContextBlueprint(self) -> Optional[RankContextBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        context = cast(Type[self._modelContext]Context, self._model)
        return RankContextBlueprint(
            persona=context.magnitude,
        )
