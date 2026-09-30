# src/transit/carrier/model/arena/carrier.py

"""
Module: transit.carrier.model.arena.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Arena, ArenaBlueprint
from transit import ModelCarrier


class ArenaCarrier(ModelCarrier[Arena]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Arena or its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [Arena|ArenaBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[ArenaBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[Arena]
    _blueprint: Optional[ArenaBlueprint]
    
    def __init__(
            self,
            model: Optional[Arena] | None = None,
            blueprint: Optional[ArenaBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Arena]
            blueprint: Optional[ArenaBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Arena|ArenaBlueprint]:
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
                isinstance(self._model, Arena)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, ArenaBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[ArenaBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(Arena, self._model)
        return ArenaBlueprint(
            id=model.id,
            game=model.game,
            board=model.board,
            player_binder=model.player_binder,
        )

