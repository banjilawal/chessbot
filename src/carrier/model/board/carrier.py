# src/carrier/board/operand.py

"""
Module: carrier.board.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import BoardBlueprint
from model import Board
from carrier import EntityCarrierToggle


class BoardCarrierToggle(EntityCarrierToggle[Board]):
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
        EntityCarrierToggle
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
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Board | BoardBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return self._model is not None and self._blueprint is None
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return self._model is None and self._blueprint is not None
    
    @property
    def is_empty(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def has_overflow(self) -> bool:
        return self._model is not None and self._blueprint is not None
    
    @property
    def size(self) -> int:
        if self.is_not_carrying_anything: return 0
        if self.is_carrying_model or self.is_carrying_blueprint: return 1
        return 2
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BoardCarrierToggle):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

