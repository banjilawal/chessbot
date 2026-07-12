# src/blueprint/register/cartesian/blueprint.py

"""
Module: blueprint.register.cartesian.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type, cast

from blueprint import RegisterBlueprint
from operand import CartesianPoint
from register import CartesianRegister


@dataclass
class CartesianRegisterBlueprint(RegisterBlueprint[CartesianRegister]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a CartesianPoint object.
    
    Attributes:
        a: CartesianPoint
        b: CartesianPoint
    
    Provides:
    
    Super Class:
        RegisterBlueprint
    """
    _a: CartesianPoint
    _b: CartesianPoint
    
    def __init__(
            self,
            a: CartesianPoint,
            b: CartesianPoint,
            model_class: Type[CartesianRegister] = CartesianRegister,
    ):
        """
        Args:
            a: CartesianPoint
            b: CartesianPoint
            model_class: Type[CartesianPoint]
        """
        super().__init__(a=a, b=b, model_class=model_class)
    
    @property
    def mode_class(self) -> Type[CartesianPoint]:
        return cast(Type[CartesianPoint], self.model_class)
    
    @property
    def a(self) -> CartesianPoint:
        return self._a
    
    @property
    def b(self) -> CartesianPoint:
        return self._b
    
    

