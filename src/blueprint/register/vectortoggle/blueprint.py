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
from chooser import VectorToggle
from err import CartesianRegisterNullException, RegisterNullException
from register import VectorToggleRegister



class CartesianRegisterBlueprint(RegisterBlueprint[VectorToggleRegister]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a VectorToggle object.
    
    Attributes:
        a: VectorToggle
        b: VectorToggle
        model_class: Optional[Type[CartesianRegister]]
        null_exception: Optional[CartesianRegisterNullException]
    
    Provides:
    
    Super Class:
        RegisterBlueprint
    """
    _a: VectorToggle
    _b: VectorToggle
    
    def __init__(
            self,
            a: VectorToggle,
            b: VectorToggle,
            model_class: Optional[Type[VectorToggleRegister]] | None = VectorToggleRegister,
            null_exception: Optional[CartesianRegisterNullException] |
                            None = CartesianRegisterNullException(),
    ):
        """
        Args:
            a: VectorToggle
            b: VectorToggle
            model_class: Optional[Type[CartesianRegister]]
            null_exception: Optional[CartesianRegisterNullException]
        """
        super().__init__(a=a, b=b, model_class=model_class, null_exception=null_exception)
    
    @property
    def model_class(self) -> Type[VectorToggle]:
        return cast(Type[VectorToggle], self.model_class)
    
    @property
    def null_exception(self) -> RegisterNullException:
        return cast(RegisterNullException, self.null_exception)
    
    @property
    def a(self) -> VectorToggle:
        return self._a
    
    @property
    def b(self) -> VectorToggle:
        return self._b
    
    

