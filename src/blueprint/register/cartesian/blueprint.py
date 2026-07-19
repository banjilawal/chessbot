# src/blueprint/register/cartesian/blueprint.py

"""
Module: blueprint.register.cartesian.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Type, cast

from blueprint import RegisterBlueprint
from chooser import CartesianPoint
from err import CartesianRegisterNullException, RegisterNullException
from register import CartesianRegister



class CartesianRegisterBlueprint(RegisterBlueprint[CartesianRegister]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a CartesianPoint object.
    
    Attributes:
        a: CartesianPoint
        b: CartesianPoint
        model_class: Optional[Type[CartesianRegister]]
        null_exception: Optional[CartesianRegisterNullException]
    
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
            model_class: Optional[Type[CartesianRegister]] | None = CartesianRegister,
            null_exception: Optional[CartesianRegisterNullException] |
                            None = CartesianRegisterNullException(),
    ):
        """
        Args:
            a: CartesianPoint
            b: CartesianPoint
            model_class: Optional[Type[CartesianRegister]]
            null_exception: Optional[CartesianRegisterNullException]
        """
        super().__init__(a=a, b=b, model_class=model_class, null_exception=null_exception)
    
    @property
    def model_class(self) -> Type[CartesianPoint]:
        return cast(Type[CartesianPoint], self.model_class)
    
    @property
    def null_exception(self) -> RegisterNullException:
        return cast(RegisterNullException, self.null_exception)
    
    @property
    def a(self) -> CartesianPoint:
        return self._a
    
    @property
    def b(self) -> CartesianPoint:
        return self._b
    
    

