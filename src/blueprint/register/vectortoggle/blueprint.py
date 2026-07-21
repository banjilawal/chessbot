# src/blueprint/register/vectortoggle/blueprint.py

"""
Module: blueprint.register.vectortoggle.blueprint
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


class VectorToggleRegisterBlueprint(RegisterBlueprint[VectorToggleRegister]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a VectorToggle object.
    
    Attributes:
        a: VectorToggle
        b: VectorToggle
        model_class: Optional[Type[VectortoggleRegister]]
        null_exception: Optional[VectortoggleRegisterNullException]
    
    Provides:
    
    Super Class:
        RegisterBlueprint
    """
    
    def __init__(
            self,
            a: VectorToggle,
            b: VectorToggle,
            model_class: Optional[Type[VectorToggleRegister]]
                         | None = VectorToggleRegister,
            null_exception: Optional[VectorToggleRegisterNullException] |
                            None = VectorToggleRegisterNullException(),
    ):
        """
        Args:
            a: VectorToggle
            b: VectorToggle
            model_class: Optional[Type[VectortoggleRegister]]
            null_exception: Optional[VectortoggleRegisterNullException]
        """
        super().__init__(
            a=a,
            b=b,
            model_class=model_class,
            null_exception=null_exception
        )
    
    @property
    def model_class(self) -> Type[VectorToggle]:
        return cast(Type[VectorToggle], self.model_class)
    
    @property
    def null_exception(self) -> VectorToggleRegisterNullException:
        return cast(VectorToggleRegisterNullException, self.null_exception)
    
    @property
    def a(self) -> VectorToggle:
        return cast(VectorToggle, super().a)
    
    @property
    def b(self) -> VectorToggle:
        return cast(VectorToggle, super().b)
    
    

