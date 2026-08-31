# src/transit/carrier/context/scalar/carrier.py

"""
Module: transit.carrier.context.scalar.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Scalar, ScalarBlueprint
from transit import ContextCarrier


class ScalarContextCarrier(ContextCarrier[ScalarContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated ScalarContext or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Scalar|ScalarContextBlueprint]

    Provides:
        - def extract_ContextBlueprint() -> Optional[ScalarContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[ScalarContext]
    _blueprint: Optional[ScalarContextBlueprint]
    
    def __init__(
            self,
            model: Optional[ScalarContext] | None = None,
            blueprint: Optional[ScalarContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[ScalarContext]
            blueprint: Optional[ScalarContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Scalar | ScalarContextBlueprint]:
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
                isinstance(self._model, Scalar)
        )
    
    @property
    def is_carrying_ContextBlueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, ScalarBlueprint)
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
    
    def extract_ContextBlueprint(self) -> Optional[ScalarContextBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        context = cast(ScalarContext, self._model)
        return ScalarContextBlueprint(
             magnitude=context.magnitude,
        )

