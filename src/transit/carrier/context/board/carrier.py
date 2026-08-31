# src/transit/carrier/context/board/carrier.py

"""
Module: transit.carrier.context.board.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Board, BoardBlueprint
from transit import ContextCarrier


class BoardContextCarrier(ContextCarrier[BoardContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated BoardContext or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Board|BoardContextBlueprint]

    Provides:
        - def extract_ContextBlueprint() -> Optional[BoardContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[BoardContext]
    _blueprint: Optional[BoardContextBlueprint]
    
    def __init__(
            self,
            model: Optional[BoardContext] | None = None,
            blueprint: Optional[BoardContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[BoardContext]
            blueprint: Optional[BoardContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Board|BoardContextBlueprint]:
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
                isinstance(self._model, Board)
        )
    
    @property
    def is_carrying_ContextBlueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, BoardBlueprint)
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
    
    def extract_ContextBlueprint(self) -> Optional[BoardContextBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        context = cast(BoardContext, self._model)
        return BoardContextBlueprint(
            id=context.id,
            arena=context.arena,
            squares=context.squares,
            maneuver_log=context.maneuver_log,
            attack_records=context.attack_records,
            captured_tokens=context.captured_tokens,
            team_binder=context.team_binder,
        )

