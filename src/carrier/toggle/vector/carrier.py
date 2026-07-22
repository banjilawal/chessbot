# src/toggle/vector/toggle.py

"""
Module: toggle.vector.toggle
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional, cast

from blueprint import VectorToggleBlueprint
from carrier.register.vector.carrier import VectorRegisterCarrierToggle
from carrier.toggle.carrier import ToggleCarrier
from model import Coord, Vector
from toggle import Toggle, VectorToggle


class VectorToggleCarrier(ToggleCarrier[VectorToggle]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Picks toggle a
                -   Coord: Geometric quantity
                -   Vector: Linear Vector
            as an toggle for multiplication, conversion or simple addition.

    Attributes:
        vector: Optional[Vector]
        coord: Optional[Coord]
        entity: Optional[Coord|Vector]
        is_coord_point: bool
        is_vector_point: bool

    Provides:
        
        -   _equal_vector_points(point: Point) -> bool
        -  _equal_coord_points(self, point: Point) -> bool
    Super Class:
        Toggle
    """
    _model: Optional[VectorToggle]
    _blueprint: Optional[VectorToggleBlueprint]
    
    def __init__(
            self,
            model: Optional[VectorToggle] | None = None,
            blueprint: Optional[VectorToggleBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[VectorToggle] | None = None,
            blueprint: Optional[VectorToggleBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [VectorToggle | VectorToggleBlueprint | None]:
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
                isinstance(self._model, VectorToggle)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, VectorToggleBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[VectorToggleBlueprint]:
        if self.is_not_carrying_anything:
            return None
        if self.is_carrying_blueprint:
            return self._blueprint
        if self._model.switched_coord_on:
            return VectorToggleBlueprint(coord=self._model.entity)
        return VectorToggleBlueprint(vector=self._model.entity)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "model": self._model,
            "blueprint": self._blueprint,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorToggleCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)
    
    