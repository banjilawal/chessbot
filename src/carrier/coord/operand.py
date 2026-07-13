# src/carrier/coord/operand.py

"""
Module: carrier.coord.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from blueprint import CoordBlueprint
from model import Coord
from chooser import EntityCarrier


class CoordCarrier(EntityCarrier[Coord]):
    """
    Role:
        -   ENTITY

    Responsibilities:
        2.  Transports either a Coord or its Blueprint.

    Attributes:
        entity: [Coord|CoordBlueprint]
        is_empty: bool
        has_overflow: bool
        is_model_operand: bool
        is_blueprint_operand: bool
        to_dict: Dict[str, Any]
        size: int

    Provides:
        -   extract_blueprint() -> Optional[CoordBlueprint]

    Super Class:
        EntityOperand
    """
    _model: Optional[Coord]
    _blueprint: Optional[CoordBlueprint]
    
    def __init__(
            self,
            model: Optional[Coord] | None = None,
            blueprint: Optional[CoordBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Coord]
            blueprint: Optional[CoordBlueprint]
        """
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Coord | CoordBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_model_operand(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Coord)
        )
    
    @property
    def is_blueprint_operand(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, CoordBlueprint)
        )

    def extract_blueprint(self) -> Optional[CoordBlueprint]:
        if self.no_active_toggles: return None
        if self.is_blueprint_operand: return self._blueprint
        return CoordBlueprint(
            row=self._model.row,
            column=self._model.column,
        )
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "model": self._model,
            "blueprint": self._blueprint
        }
    
    @property
    def is_empty(self) -> bool:
        return len(self.to_dict) == 0
    
    @property
    def is_full(self) -> bool:
        return len(self.to_dict) == 1
    
    @property
    def has_overflow(self) -> bool:
        return len(self.to_dict) >= 2
    
    @property
    def size(self) -> int:
        return len(self.to_dict)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CoordCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

