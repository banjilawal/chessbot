# src/transit/carrier/context/player/carrier.py

"""
Module: transit.carrier.context.player.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import PlayerBlueprint, PlayerContext, PlayerContextBlueprint
from transit import ContextCarrier


class PlayerContextCarrier(ContextCarrier[PlayerContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated PlayerContext or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [Player|PlayerContextBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[PlayerContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[PlayerContext]
    _blueprint: Optional[PlayerContextBlueprint]
    
    def __init__(
            self,
            model: Optional[PlayerContext] | None = None,
            blueprint: Optional[PlayerContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[PlayerContext]
            blueprint: Optional[PlayerContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[PlayerContext | PlayerContextBlueprint]:
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
                isinstance(self._model, PlayerContext)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None and
                isinstance(self._blueprint, PlayerContextBlueprint)
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_consistent(self) -> bool:
        return self.size > 1
    
    def extract_blueprint(self) -> Optional[PlayerContextBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(PlayerContext, self._model)
        return PlayerContextBlueprint(
            id=model.id,
            account=model.account,
            game=model.game,
            player_type=model.player_type,
        )
    
    



