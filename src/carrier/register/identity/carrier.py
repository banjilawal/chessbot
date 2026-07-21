# src/carrier/register/identity/operand.py

"""
Module: carrier.register.identity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from _ast import Dict
from typing import Any, Optional, cast

from blueprint import IdentityRegisterBlueprint
from carrier import RegisterCarrierToggle
from register import IdentityRegister


class IdentityRegisterCarrierToggle(RegisterCarrierToggle[IdentityRegister]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either an IdentityRegister or IdentityRegisterBlueprint
    
    Attributes:
        model: Optional[IdentityRegister]
        blueprint: Optional[IdentityRegisterBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        RegisterEntityCarrierToggle
    """
    _model: Optional[IdentityRegister]
    _blueprint: Optional[IdentityRegisterBlueprint]
    
    def __init__(
            self,
            model: Optional[IdentityRegister] | None = None,
            blueprint: Optional[IdentityRegisterBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[IdentityRegister] | None = None,
            blueprint: Optional[IdentityRegisterBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [IdentityRegister | IdentityRegisterBlueprint | None]:
        if self.no_active_toggles:
            return None
        if self.is_model_carrier:
            return self._blueprint
        return self._blueprint
    
    @property
    def is_model_carrier(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, IdentityRegister)
        )
    
    @property
    def is_blueprint_carrier(self) -> bool:
        return (
                not self.is_model_carrier and
                isinstance(self._blueprint, IdentityRegisterBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[IdentityRegisterBlueprint]:
        if self.no_active_toggles:
            return None
        if self.is_blueprint_carrier:
            return self._blueprint
        return IdentityRegisterBlueprint(
            id=self._model.id,
            name=self._model.name,
        )
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "model": self._model,
            "blueprint": self._blueprint,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, RegisterCarrierToggle):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

