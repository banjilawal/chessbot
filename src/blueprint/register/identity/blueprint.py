# src/blueprint/register/identity/blueprint.py

"""
Module: blueprint.register.identity.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import  annotations

from typing import Type, cast

from blueprint import RegisterBlueprint
from err import IdentityRegisterNullException
from register import IdentityRegister


class IdentityRegisterBlueprint(RegisterBlueprint[IdentityRegister]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a IdentityRegister object.

    Attributes:
        id: int
        name: str
        model_class: Type[IdentityRegister]
        null_exception: IdentityRegisterNullException
    Provides:

    Super Class:
        RegisterBlueprint
    """
    
    def __init__(
            self,
            id: int,
            name: str,
            model_class: Type[IdentityRegister] = IdentityRegister,
            null_exception: IdentityRegisterNullException |
                            None = IdentityRegisterNullException(),
    ):
        """
        Args:
            id: int
            name: str
            model_class: Type[IdentityRegister]
            null_exception: IdentityRegisterNullException
        """
        super().__init__(
            a=id,
            b=name,
            model_class=model_class,
            null_exception=null_exception,
        )
    
    @property
    def model_class(self) -> Type[IdentityRegister]:
        return cast(Type[IdentityRegister], self.model_class)
    
    @property
    def id(self) -> int:
        return cast(int, self.a)
    
    @property
    def name(self) -> str:
        return cast(str, self.b)

