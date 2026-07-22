# src/blueprint/register/toggle/blueprint.py

"""
Module: blueprint.register.toggle.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from blueprint import RegisterBlueprint
from err import VectorToggleRegisterNullException
from register import VectorToggleRegister
from toggle import VectorToggle


class VectorToggleRegisterBlueprint(
    RegisterBlueprint[VectorToggleRegister]
):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a VectorToggle object.
    
    Attributes:
        a: VectorToggle
        b: VectorToggle
        model_class: Optional[Type[VectorToggleRegister]]
        null_exception: Optional[VectorToggleRegisterNullException]
    
    Provides:
    
    Super Class:
        RegisterBlueprint
    """
    
    def __init__(
            self,
            u: VectorToggle,
            v: VectorToggle,
            model_class: Optional[Type[VectorToggleRegister]]
                         | None = VectorToggleRegister,
            null_exception: Optional[VectorToggleRegisterNullException] |
                            None = VectorToggleRegisterNullException(),
    ):
        """
        Args:
            u: VectorToggle
            v: VectorToggle
            model_class: Optional[Type[VectorToggleRegister]]
            null_exception: Optional[VectorToggleRegisterNullException]
        """
        super().__init__(
            a=u,
            b=v,
            model_class=model_class,
            null_exception=null_exception
        )
    
    @property
    def model_class(self) -> Type[VectorToggle]:
        return cast(Type[VectorToggle], super().model_class)
    
    @property
    def null_exception(self) -> VectorToggleRegisterNullException:
        return cast(VectorToggleRegisterNullException, super().null_exception)
    
    @property
    def a(self) -> VectorToggle:
        return cast(VectorToggle, super().a)
    
    @property
    def b(self) -> VectorToggle:
        return cast(VectorToggle, super().b)
    
    @property
    def toggles_are_same_type(self) -> bool:
        return isinstance(self.a.entity, type(self.b.entity))
    
    @property
    def toggles_are_different_types(self) -> bool:
        return not self.toggles_are_same_type
    
    

