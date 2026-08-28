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
        1.  Metadata
    
    Responsibilities:
        1.  Provides values for hydrating a CartesianToggle object.
    
    Attributes:
        a: CartesianToggle
        b: CartesianToggle
        domain_class: Optional[Type[CartesianToggleRegister]]
        domain_null_exception: Optional[CartesianToggleRegisterNullException]
    
    Provides:
    
    Super Class:
        RegisterBlueprint
    """
    
    def __init__(
            self,
            u: CartesianToggle,
            v: CartesianToggle,
            domain_class: Optional[Type[CartesianToggleRegister]]
                         | None = CartesianToggleRegister,
            domain_null_exception: Optional[CartesianToggleRegisterNullException] |
                            None = CartesianToggleRegisterNullException(),
    ):
        """
        Args:
            u: CartesianToggle
            v: CartesianToggle
            domain_class: Optional[Type[CartesianToggleRegister]]
            domain_null_exception: Optional[CartesianToggleRegisterNullException]
        """
        super().__init__(
            a=u,
            b=v,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def domain_class(self) -> Type[CartesianToggle]:
        return cast(Type[CartesianToggle], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CartesianToggleRegisterNullException:
        return cast(CartesianToggleRegisterNullException, super().domain_null_exception)
    
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
    
    

