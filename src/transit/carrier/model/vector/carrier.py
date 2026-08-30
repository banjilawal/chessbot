# src/transit/carrier/model/mode/vector/carrier.py

"""
Module: transit.carrier.model.model.vector.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import Vector, VectorBlueprint
from transit import ModelCarrier


class VectorCarrier(ModelCarrier[Vector]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Vector or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Vector|VectorBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[VectorBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[Vector]
    _blueprint: Optional[VectorBlueprint]
    
    def __init__(
            self,
            model: Optional[Vector] | None = None,
            blueprint: Optional[VectorBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Vector]
            blueprint: Optional[VectorBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Vector|VectorBlueprint]:
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
                isinstance(self._model, Vector)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, VectorBlueprint)
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
     
    def extract_blueprint(self) -> Optional[VectorBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        return VectorBlueprint(
            x=self._model.x,
            y=self._model.y,
        )

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

