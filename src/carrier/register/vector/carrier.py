# src/carrier/register/vector/operand.py

"""
Module: carrier.register.vector.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast


from carrier import EntityCarrierToggle, RegisterCarrier
from register import VectorRegister


class VectorRegisterCarrierToggle(EntityCarrierToggle[VectorRegister]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either an VectorRegister or VectorRegisterBlueprint
    
    Attributes:
        model: Optional[VectorRegister]
        blueprint: Optional[VectorRegisterBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        RegisterEntityCarrierToggle
    """
    _model: Optional[VectorRegister]
    _blueprint: Optional[VectorRegisterBlueprint]
    
    def __init__(
            self,
            model: Optional[VectorRegister] | None = None,
            blueprint: Optional[VectorRegisterBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Register]
            blueprint: Optional[RegisterBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
        
    @property
    def entity(self) -> [VectorRegister | VectorRegisterBlueprint | None]:
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
                isinstance(self._model, VectorRegister)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return not (
                self.is_carrying_model and
                isinstance(self._blueprint, VectorRegisterBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[VectorRegisterBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return VectorRegisterBlueprint(
            id=self._model.id,
            u=self._model.u,
            v=self._model.v,
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
        if isinstance(other, RegisterCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

