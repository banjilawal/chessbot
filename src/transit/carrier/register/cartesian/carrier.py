# src/transit/carrier/structure/register/point/carrier.py

"""
Module: transit.carrier.structure.register.point.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import CartesianToggle
from transit import RegisterCarrier


class CartesianToggleRegisterCarrier(RegisterCarrier[CartesianToggle]):
    """
    Role:
        - Addressing
        -  Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either a CartesianToggleRegister or CartesianToggleRegisterBlueprint
    
    Attributes:
        model: Optional[CartesianToggleRegister]
        blueprint: Optional[CartesianToggleRegisterBlueprint]
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
            model: Optional[CartesianToggleRegister] |
                   None = None,
            blueprint: Optional[CartesianToggleRegisterBlueprint] |
                       None = None,
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
    def entity(self) -> [CartesianToggleRegister | CartesianToggleRegisterBlueprint | None]:
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
                isinstance(self._model, CartesianToggleRegister)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return not (
                self.is_carrying_model and
                isinstance(self._blueprint, CartesianToggleRegisterBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[CartesianToggleRegisterBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return CartesianToggleRegisterBlueprint(
            u=self._model.a,
            v=self._model.b,
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
        if isinstance(other, RegisterCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

