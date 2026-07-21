# src/blueprint/register/number/blueprint.py

"""
Module: blueprint.register.number.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from blueprint import RegisterBlueprint
from err import NumberRegisterNullException
from register import NumberRegister


class NumberRegisterBlueprint(RegisterBlueprint[NumberRegister]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a NumberRegister object.

    Attributes:
        origin: Number
        destination: Number
        model_class: Type[NumberRegister]
        null_exception: Optional[NumberRegisterNullException]

    Provides:

    Super Class:
        RegisterBlueprint
    """
    
    def __init__(
            self,
            a: int,
            b: int,
            model_class: Type[NumberRegister] = NumberRegister,
            null_exception: Optional[NumberRegisterNullException] |
                            None = NumberRegisterNullException(),
    ):
        """
        Args:
            a: int
            b: int
            model_class: Type[NumberRegister]
            null_exception: Optional[NumberRegisterNullException]
        """
        super().__init__(a=a, b=b, model_class=model_class, null_exception=null_exception)
    
    @property
    def model_class(self) -> Type[NumberRegister]:
        return cast(Type[NumberRegister], super().model_class)
    
    @property
    def a(self) -> int:
        return cast(int, self.a)
    
    @property
    def b(self) -> int:
        return cast(int, self.b)
    
    @property
    def null_exception(self) -> NumberRegisterNullException:
        return cast(NumberRegisterNullException, super().null_exception)
