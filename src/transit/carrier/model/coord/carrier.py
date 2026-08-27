# src/transit/carrier/coord/carrier.py

"""
Module: transit.carrier.coord.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from transit.metadata.blueprint import CoordBlueprint
from transit.model import Coord
from carrier import ModelCarrier


class CoordCarrier(ModelCarrier[Coord]):
    """
    Role:
        - Data Transport

    Responsibilities:
        2.  Transports either a Coord or its Blueprint.

    Attributes:
        entity: [Coord|CoordBlueprint]
        is_empty: bool
        has_overflow: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        to_dict: Dict[str, Any]
        size: int

    Provides:
        -  extract_blueprint() -> Optional[CoordBlueprint]

    Super Class:
        ModelCarrier
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
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Coord | CoordBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Coord)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, CoordBlueprint)
        )

    def extract_blueprint(self) -> Optional[CoordBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return CoordBlueprint(
            row=self._model.row,
            column=self._model.column,
        )

    
    @property
    def is_empty(self) -> bool:
        return len(self.to_dict) == 0
    
    @property
    def is_full(self) -> bool:
        return len(self.to_dict) == 1
    
    @property
    def is_not_carrying_anything(self) -> bool:
        return len(self.to_dict) >= 2
    
    @property
    def size(self) -> int:
        return len(self.to_dict)
        
    @property
    def is_not_carrying_anything(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def is_carrying_too_much(self) -> bool:
        return not self.is_not_carrying_anything

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CoordCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

