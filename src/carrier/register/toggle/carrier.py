# src/carrier/register/point/operand.py

"""
Module: carrier.register.point.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import VectorToggleRegisterBlueprint
from carrier import RegisterCarrier
from register import VectorToggleRegister
from toggle import VectorToggle


class VectorToggleRegisterCarrier(RegisterCarrier[VectorToggle]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either an VectorToggleRegister or VectorToggleRegisterBlueprint
    
    Attributes:
        model: Optional[VectorToggleRegister]
        blueprint: Optional[VectorToggleRegisterBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        RegisterEntityCarrierToggle
    """
    
    def __init__(
            self,
            model: Optional[VectorToggleRegister] | None = None,
            blueprint: Optional[VectorToggleRegisterBlueprint] | None = None,
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
    def entity(self) -> [VectorToggleRegister | VectorToggleRegisterBlueprint | None]:
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
                isinstance(self._model, VectorToggleRegister)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return not (
                self.is_carrying_model and
                isinstance(self._blueprint, VectorToggleRegisterBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[VectorToggleRegisterBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return VectorToggleRegisterBlueprint(
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

