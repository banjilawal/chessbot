# src/transit/carrier/scalar/carrier.py

"""
Module: transit.carrier.scalar.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from transit.metadata.blueprint import ScalarBlueprint
from transit.model import Scalar
from carrier import ModelCarrier


class ScalarCarrier(ModelCarrier[Scalar]):
    """
    Role:
        -  Addressing
        -  Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either a Scalar or ScalarBlueprint
    
    Attributes:
        model: Optional[Scalar]
        blueprint: Optional[ScalarBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
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
    def entity(self) -> [Scalar | ScalarBlueprint | None]:
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
                isinstance(self._model, Scalar)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, ScalarBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[ScalarBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return ScalarBlueprint(
             magnitude=self._model.magnitude,
        )
        
    @property
    def is_not_carrying_anything(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def is_carrying_too_much(self) -> bool:
        return not self.is_not_carrying_anything

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ScalarCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

