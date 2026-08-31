# src/transit/carrier/model/coord/carrier.py

"""
Module: transit.carrier.model.coord.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Coord, CoordBlueprint
from transit import ModelCarrier


class CoordCarrier(ModelCarrier[Coord]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Coord or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Coord|CoordBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[CoordBlueprint]

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
    def entity(self) -> Optional[Coord | CoordBlueprint]:
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
                isinstance(self._model, Coord)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, CoordBlueprint)
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
    
    def extract_blueprint(self) -> Optional[CoordBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(Coord, self._model)
        return CoordBlueprint(
            row=model.row,
            column=model.column,
        )

