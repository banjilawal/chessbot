# src/transit/carrier/context/game/carrier.py

"""
Module: transit.carrier.context.game.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import GameContext, GameContextBlueprint
from transit import ContextCarrier


class GameContextCarrier(ContextCarrier[GameContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated GameContext or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [GameContext | GameContextBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[GameContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[GameContext]
    _blueprint: Optional[GameContextBlueprint]
    
    def __init__(
            self,
            model: Optional[GameContext] | None = None,
            blueprint: Optional[GameContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[GameContext]
            blueprint: Optional[GameContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[GameContext | GameContextBlueprint]:
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
                isinstance(self._model, GameContext)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None and
                isinstance(self._blueprint, GameContextBlueprint)
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
    
    def extract_blueprint(self) -> Optional[GameContextBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(GameContext, self._model)
        return GameContextBlueprint(
            id=model.id,
            arena=model.arena,
            validation_state=model.state,
            player=model.player,
            account=model.account,
        )

