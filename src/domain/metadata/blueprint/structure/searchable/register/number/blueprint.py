# src/domain/metadata/blueprint/structure/register/number/blueprint.py

"""
Module: domain.metadata.blueprint.structure.register.number.blueprint.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain.metadata.blueprint.structure import RegisterBlueprint
from err import NumberRegisterNullException
from domain.structure.searchable.register import NumberRegister


class NumberRegisterBlueprint(RegisterBlueprint[NumberRegister]):
    """
    Role:
        - Container

    Responsibilities:
        1.  Provides values for hydrating a NumberRegister object.

    Attributes:
        origin: Number
        destination: Number
        domain_class: Type[NumberRegister]
        domain_null_exception: Optional[NumberRegisterNullException]

    Provides:

    Super Class:
        RegisterBlueprint
    """
    
    def __init__(
            self,
            a: int,
            b: int,
            domain_class: Type[NumberRegister] = NumberRegister,
            domain_null_exception: Optional[NumberRegisterNullException] |
                            None = NumberRegisterNullException(),
    ):
        """
        Args:
            a: int
            b: int
            domain_class: Type[NumberRegister]
            domain_null_exception: Optional[NumberRegisterNullException]
        """
        super().__init__(a=a, b=b, domain_class=domain_class, domain_null_exception=domain_null_exception)
    
    @property
    def domain_class(self) -> Type[NumberRegister]:
        return cast(Type[NumberRegister], super().domain_class)
    
    @property
    def a(self) -> int:
        return cast(int, self.a)
    
    @property
    def b(self) -> int:
        return cast(int, self.b)
    
    @property
    def domain_null_exception(self) -> NumberRegisterNullException:
        return cast(NumberRegisterNullException, super().domain_null_exception)
