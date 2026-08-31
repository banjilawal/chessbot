# src/transit/carrier/context/arena/carrier.py

"""
Module: transit.carrier.context.arena.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Arena, ArenaBlueprint
from transit import ContextCarrier


class ArenaContextCarrier(ContextCarrier[ArenaContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated ArenaContext or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Arena|ArenaContextBlueprint]

    Provides:
        - def extract_ContextBlueprint() -> Optional[ArenaContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[ArenaContext]
    _blueprint: Optional[ArenaContextBlueprint]
    
    def __init__(
            self,
            model: Optional[ArenaContext] | None = None,
            blueprint: Optional[ArenaContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[ArenaContext]
            blueprint: Optional[ArenaContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Arena|ArenaContextBlueprint]:
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
                isinstance(self._model, Arena)
        )
    
    @property
    def is_carrying_ContextBlueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, ArenaBlueprint)
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
    
    def extract_ContextBlueprint(self) -> Optional[ArenaContextBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        context = cast(ArenaContext, self._model)
        return ArenaContextBlueprint(
            id=context.id,
            game=context.game,
            board=context.board,
            player_binder=context.player_binder,
        )

