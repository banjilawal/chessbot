# src/carrier/scalar/operand.py

"""
Module: carrier.scalar.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from blueprint import ScalarBlueprint
from model import Scalar
from carrier import EntityCarrierToggle


class ScalarCarrierToggle(EntityCarrierToggle[Scalar]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
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
        EntityCarrierToggle
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
        super()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Scalar | ScalarBlueprint | None]:
        if self.no_active_toggles:
            return None
        if self.is_model_carrier:
            return self._model
        return self._blueprint
    
    @property
    def is_model_carrier(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Scalar)
        )
    
    @property
    def is_blueprint_carrier(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, ScalarBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[ScalarBlueprint]:
        if self.no_active_toggles: return None
        if self.is_blueprint_carrier: return self._blueprint
        return ScalarBlueprint(
             magnitude=self._model.magnitude,
        )
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "model": self._model,
            "blueprint": self._blueprint
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ScalarCarrierToggle):
            return self.entity == other.entity
        return False
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ScalarCarrierToggle):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

