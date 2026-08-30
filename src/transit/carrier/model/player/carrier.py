# src/transit/carrier/model/mode/player/carrier.py

"""
Module: transit.carrier.model.model.player.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import Player, PlayerBlueprint
from transit import ModelCarrier


class PlayerCarrier(ModelCarrier[Player]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Player or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Player|PlayerBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[PlayerBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[Player]
    _blueprint: Optional[PlayerBlueprint]
    
    def __init__(
            self,
            model: Optional[Player] | None = None,
            blueprint: Optional[PlayerBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Player]
            blueprint: Optional[PlayerBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Player | PlayerBlueprint]:
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
                isinstance(self._model, Player)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, PlayerBlueprint)
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
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PlayerCarrier):
            return self.entity == other.entity
        return False


