# src/carrier/board/carrier.py

"""
Module: carrier.board.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import BoardBlueprint
from model import Board
from carrier import ModelCarrier


class BoardCarrier(ModelCarrier[Board]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either a Board or BoardBlueprint
    
    Attributes:
        model: Optional[Board]
        blueprint: Optional[BoardBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
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
    def entity(self) -> [Board | BoardBlueprint]:
        return self._model or self._blueprint
    
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
    def is_not_carrying_anything(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def is_carrying_too_much(self) -> bool:
        return not self.is_not_carrying_anything

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BoardCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

