# src/transit/carrier/model/vector/carrier.py

"""
Module: transit.carrier.model.vector.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Vector, VectorBlueprint
from transit import ModelCarrier

class VectorCarrier(ModelCarrier[Vector]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Vector or its Blueprint.

    Attributes:
        model: Optional[Vector]
        blueprint: Optional[VectorBlueprint]
        entity: [Vector | VectorBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[VectorBlueprint]

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
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Vector | VectorBlueprint]:
        if self.has_model:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Vector)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, VectorBlueprint)
        )
     
    def extract_blueprint(self) -> Optional[VectorBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(Vector, self._model)
        return VectorBlueprint(
            x=model.x,
            y=model.y,
        )

