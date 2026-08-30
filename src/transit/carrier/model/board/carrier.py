# src/transit/carrier/model/mode/board/carrier.py

"""
Module: transit.carrier.model.model.board.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import Board, BoardBlueprint
from transit import ModelCarrier


class BoardCarrier(ModelCarrier[Board]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Board or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Board|BoardBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[BoardBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[Board]
    _blueprint: Optional[BoardBlueprint]
    
    def __init__(
            self,
            model: Optional[Board] | None = None,
            blueprint: Optional[BoardBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Board]
            blueprint: Optional[BoardBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Board | BoardBlueprint]:
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
    def is_carrying_blueprint(self) -> bool:
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
    def over_capacity(self) -> bool:
        return self.size > 1
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BoardCarrier):
            return self.entity == other.entity
        return False

