# src/carrier/register/identity/operand.py

"""
Module: carrier.register.identity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import IdentityRegisterBlueprint
from model import IdentityRegister
from operand import RegisterCarrier


class IdentityRegisterEntityOperand(RegisterCarrier[IdentityRegister]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either an IdentityRegister or IdentityRegisterBlueprint
    
    Attributes:
        model: Optional[IdentityRegister]
        blueprint: Optional[IdentityRegisterBlueprint]
        is_model_operand: bool
        is_blueprint_operand: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        RegisterEntityOperand
    """
    
    def __init__(
            self,
            model: Optional[IdentityRegister] | None = None,
            blueprint: Optional[IdentityRegisterBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Register]
            blueprint: Optional[RegisterBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    def entity(self) -> [IdentityRegister | IdentityRegisterBlueprint]:
        if self.is_empty:
            return None
        if self.is_model_operand:
            return cast(IdentityRegister, self.entity)
        return cast(IdentityRegisterBlueprint, self.entity)
    
    @property
    def is_model_operand(self) -> bool:
        return self._model is not None and self._blueprint is None
    
    @property
    def is_blueprint_operand(self) -> bool:
        return self._model is None and self._blueprint is not None
    
    @property
    def is_empty(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def has_overflow(self) -> bool:
        return self._model is not None and self._blueprint is not None
    
    @property
    def size(self) -> int:
        if self.is_empty: return 0
        if self.is_model_operand or self.is_blueprint_operand: return 1
        return 2
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, RegisterCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

