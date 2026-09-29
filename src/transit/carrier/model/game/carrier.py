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
        1.  Transport a hydrated Game or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Game|GameBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[GameBlueprint]

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
        if self.has_model:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Game)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, GameBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[GameBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(Game, self._model)
        return GameBlueprint(
            id=model.id,
            arena=model.arena,
            binder=model.binder,
            checkmate=model.checkmate,
            stalemate=model.stalemate,
            turn_service=model.turn_service,
        )
