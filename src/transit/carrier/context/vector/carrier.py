# src/transit/carrier/context/vector/carrier.py

"""
Module: transit.carrier.context.vector.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Vector, VectorBlueprint, VectorContext, VectorContextBlueprint
from transit import ContextCarrier


class VectorContextCarrier(ContextCarrier[VectorContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated VectorContext or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Vector|VectorContextBlueprint]

    Provides:
        - def extract_ContextBlueprint() -> Optional[VectorContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[VectorContext]
    _blueprint: Optional[VectorContextBlueprint]
    
    def __init__(
            self,
            model: Optional[VectorContext] | None = None,
            blueprint: Optional[VectorContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[VectorContext]
            blueprint: Optional[VectorContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Vector|VectorContextBlueprint]:
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
    def is_carrying_ContextBlueprint(self) -> bool:
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
    def is_over_capacity(self) -> bool:
        return self.size > 1
     
    def extract_ContextBlueprint(self) -> Optional[VectorContextBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        context = cast(VectorContext, self._model)
        return VectorContextBlueprint(
            x=context.x,
            y=context.y,
        )

