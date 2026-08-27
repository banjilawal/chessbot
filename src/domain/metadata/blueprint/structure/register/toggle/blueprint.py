# src/domain/metadata/blueprint/structure/register/toggle/blueprint.py

"""
Module: domain.metadata.blueprint.structure.register.toggle.blueprint.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain.metadata.blueprint.structure import RegisterBlueprint
from err import CartesianToggleRegisterNullException
from domain.structure.register import CartesianToggleRegister
from domain.structure.toggle import CartesianToggle


class CartesianToggleRegisterBlueprint(
    RegisterBlueprint[CartesianToggleRegister]
):
    """
    Role:
        - Container
    
    Responsibilities:
        1.  Provides values for instantiating a CartesianToggle object.
    
    Attributes:
        a: CartesianToggle
        b: CartesianToggle
        model_class: Optional[Type[CartesianToggleRegister]]
        null_exception: Optional[CartesianToggleRegisterNullException]
    
    Provides:
    
    Super Class:
        RegisterBlueprint
    """
    
    def __init__(
            self,
            u: CartesianToggle,
            v: CartesianToggle,
            model_class: Optional[Type[CartesianToggleRegister]]
                         | None = CartesianToggleRegister,
            null_exception: Optional[CartesianToggleRegisterNullException] |
                            None = CartesianToggleRegisterNullException(),
    ):
        """
        Args:
            u: CartesianToggle
            v: CartesianToggle
            model_class: Optional[Type[CartesianToggleRegister]]
            null_exception: Optional[CartesianToggleRegisterNullException]
        """
        super().__init__(
            a=u,
            b=v,
            model_class=model_class,
            null_exception=null_exception
        )
    
    @property
    def model_class(self) -> Type[CartesianToggle]:
        return cast(Type[CartesianToggle], super().model_class)
    
    @property
    def null_exception(self) -> CartesianToggleRegisterNullException:
        return cast(CartesianToggleRegisterNullException, super().null_exception)
    
    @property
    def u(self) -> CartesianToggle:
        return cast(CartesianToggle, super().a)
    
    @property
    def v(self) -> CartesianToggle:
        return cast(CartesianToggle, super().b)
    
    @property
    def a(self) -> CartesianToggle:
        return self.u
    
    @property
    def b(self) -> CartesianToggle:
        return self.v
    
    @property
    def toggles_are_same_type(self) -> bool:
        return isinstance(self.a.entity, type(self.b.entity))
    
    @property
    def toggles_are_different_types(self) -> bool:
        return not self.toggles_are_same_type
    
    

