# src/transit/carrier/model/scalar/carrier.py

"""
Module: transit.carrier.model.scalar.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Scalar, ScalarBlueprint
from transit import ModelCarrier


class ScalarCarrier(ModelCarrier[Scalar]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Scalar or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Scalar|ScalarBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[ScalarBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[Scalar]
    _blueprint: Optional[ScalarBlueprint]
    
    def __init__(
            self,
            model: Optional[Scalar] | None = None,
            blueprint: Optional[ScalarBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Scalar]
            blueprint: Optional[ScalarBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Scalar | ScalarBlueprint]:
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
    def is_carrying_blueprint(self) -> bool:
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
    
    def extract_blueprint(self) -> Optional[ScalarBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(Scalar, self._model)
        return ScalarBlueprint(
             magnitude=model.magnitude,
        )

