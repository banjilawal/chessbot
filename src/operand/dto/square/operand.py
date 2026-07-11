# src/operand/dto/square/operand.py

"""
Module: operand.dto.square.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import SquareBlueprint
from model import HomeSquare, Square
from operand import DtoOperand


class SquareDtoOperand(DtoOperand[Square]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Dto for transporting either a Square or SquareBlueprint
    
    Attributes:
        model: Optional[Square]
        blueprint: Optional[SquareBlueprint]
        is_model_operand: bool
        is_blueprint_operand: bool
        has_overflow: bool
        is_empty: bool
        is_home_square_operand: bool
    
    Provides:
        -   extract_blueprint() -> Optional[SquareBlueprint]
    
    Super Class:
        DtoOperand
    """
    _model: Optional[Square]
    _blueprint: Optional[SquareBlueprint]
    
    def __init__(
            self,
            model: Optional[Square] | None = None,
            blueprint: Optional[SquareBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Square]
            blueprint: Optional[SquareBlueprint]
        """
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Square | SquareBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_model_operand(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Square)
        )
    
    @property
    def is_blueprint_operand(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, SquareBlueprint)
        )
    
    @property
    def is_home_square_operand(self) -> bool:
        return (
            (self.is_model_operand and
                isinstance(self._model, HomeSquare) and
                self._model.formation is not None
             ) or
            self._blueprint and self._blueprint.formation is not None
        )
    
    @property
    def is_empty(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def has_overflow(self) -> bool:
        return self._model is not None and self._blueprint is not None
    
    @property
    def size(self) -> int:
        if self.is_empty: return 0
        if self.is_model_operand or self.is_blueprint_operand: return 1
        return 2
    
    def extract_blueprint(self) -> Optional[SquareBlueprint]:
        if self.is_empty: return None
        if self.is_blueprint_operand: return self._blueprint
        if self.is_home_square_operand:
            home_square = cast(HomeSquare, self._model)
            return SquareBlueprint(
                id=home_square.id,
                board=home_square.board,
                coord=home_square.coord,
                formation=home_square.formation,
            )
        return SquareBlueprint(
            id=self._model.id,
            board=self._model.board,
            coord=self._model.coord,
        )
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SquareDtoOperand):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

