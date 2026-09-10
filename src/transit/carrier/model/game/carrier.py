# src/transit/carrier/model/game/carrier.py

"""
Module: transit.carrier.model.game.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Game, GameBlueprint
from transit import ModelCarrier


class GameCarrier(ModelCarrier[Game]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Game or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Game|GameBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[GameBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[Game]
    _blueprint: Optional[GameBlueprint]
    
    def __init__(
            self,
            model: Optional[Game] | None = None,
            blueprint: Optional[GameBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Game]
            blueprint: Optional[GameBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Game|GameBlueprint]:
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
                isinstance(self._model, Game)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, GameBlueprint)
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
    
    def extract_blueprint(self) -> Optional[GameBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(Game, self._model)
        return GameBlueprint(
            traveller=model.traveller,
            path=model.path,
            benefit=model.benefit,
            attack=model.attack,
        )

