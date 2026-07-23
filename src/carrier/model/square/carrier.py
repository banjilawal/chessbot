# src/carrier/square/carrier.py

"""
Module: carrier.square.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from blueprint import SquareBlueprint
from model import HomeSquare, Square
from carrier import EntityCarrier


class SquareCarrier(EntityCarrier[Square]):
    """
    Role:
        -   ENTITY

    Responsibilities:
        2.  Transports either a Square or its Blueprint.

    Attributes:
        entity: [Square|SquareBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        
        is_empty: bool
        has_overflow: bool
        to_dict: Dict[str, Any]
        size: int

    Provides:
        -   extract_blueprint() -> Optional[SquareBlueprint]

    Super Class:
        EntityCarrierToggle
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
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Square | SquareBlueprint | None]:
        if self.is_not_carrying_anything:
            return None
        if self.is_carrying_model:
            return self._model
        return self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Square)
        )
    
    @property
    def is_home_square_carrier(self) -> bool:
        return (
                self.is_carrying_model and
                isinstance(self._model, HomeSquare)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, SquareBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[SquareBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        if self.is_home_square_carrier:
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
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "model": self._model,
            "blueprint": self._blueprint
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SquareCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)
