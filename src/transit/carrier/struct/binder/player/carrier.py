# src/transit/carrier/struct/binder/player/carrier.py

"""
Module: transit.carrier.struct.binder.player.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import PlayerBinder, PlayerBinderBlueprint
from transit import BinderCarrier


class PlayerBinderCarrier(BinderCarrier[PlayerBinder]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated PlayerBinder its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [PlayerBinder | PlayerBinderBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[PlayerBinderBlueprint]

    Super Class:
        BinderCarrier
    """
    _model: Optional[PlayerBinder]
    _blueprint: Optional[PlayerBinderBlueprint]
    
    def __init__(
            self,
            model: Optional[PlayerBinder] | None = None,
            blueprint: Optional[PlayerBinderBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[PlayerBinder]
            blueprint: Optional[PlayerBinderBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[PlayerBinder | PlayerBinderBlueprint]:
        if self._model is not None:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._blueprint is None and
                self._model is not None and
                isinstance(self._model, PlayerBinder)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._blueprint is not None and
                self._model is None and
                isinstance(self._blueprint, PlayerBinderBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[PlayerBinderBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            return self._blueprint
        model = cast(PlayerBinder, self._model)
        return PlayerBinderBlueprint(
            white_player=model.white_player,
            black_player=model.black_player,
        )


    