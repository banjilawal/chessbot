# src/carrier/register/square/operand.py

"""
Module: carrier.register.square.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from _ast import Dict
from typing import Any, Optional, Type, cast

from blueprint import SquareRegisterBlueprint
from carrier import EntityCarrierToggle
from err import SquareRegisterNullException
from register import SquareRegister


class SquareRegisterCarrierToggle(EntityCarrierToggle[SquareRegister]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either an SquareRegister or SquareRegisterBlueprint
    
    Attributes:
        model: Optional[SquareRegister]
        blueprint: Optional[SquareRegisterBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        RegisterEntityCarrierToggle
    """
    _model: Optional[SquareRegister]
    _blueprint: Optional[SquareRegisterBlueprint]
    
    def __init__(
            self,
            model: Optional[SquareRegister] | None = None,
            blueprint: Optional[SquareRegisterBlueprint] | None = None,
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
    def entity(self) -> [SquareRegister | SquareRegisterBlueprint | None]:
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
                isinstance(self._model, SquareRegister)
        )
    
    @property
    def is_blueprint_carrier(self) -> bool:
        return not (
                self.is_model_carrier and
                isinstance(self._blueprint, SquareRegisterBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[SquareRegisterBlueprint]:
        if self.no_active_toggles: return None
        if self.is_blueprint_carrier: return self._blueprint
        return SquareRegisterBlueprint(
            origin=self._model.origin,
            destination=self._model.destination,
            model_class=Type[SquareRegister],
            null_exception=SquareRegisterNullException(),
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

