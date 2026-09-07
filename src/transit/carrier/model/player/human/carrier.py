# src/transit/carrier/model/player/human/carrier.py

"""
Module: transit.carrier.model.player.human.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import HumanPlayer, HumanBlueprint
from transit import PlayerCarrier


class HumanCarrier(PlayerCarrier):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated HumanPlayer or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [HumanPlayer|HumanBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[HumanBlueprint]

    Super Class:
        HumanPlayerCarrier
    """
    
    _model: Optional[HumanPlayer]
    _blueprint: Optional[HumanBlueprint]
    
    def __init__(
            self,
            model: Optional[HumanPlayer] | None = None,
            blueprint: Optional[HumanBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[HumanPlayer]
            blueprint: Optional[HumanBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[HumanPlayer|HumanBlueprint]:
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
                isinstance(self._model, HumanPlayer)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, HumanBlueprint)
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
    
    def extract_blueprint(self) -> Optional[HumanBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(HumanPlayer, self._model)
        return HumanBlueprint(
            id=model.id,
            name=model.name,
            adviser=model.adviser,
        )
    
    



