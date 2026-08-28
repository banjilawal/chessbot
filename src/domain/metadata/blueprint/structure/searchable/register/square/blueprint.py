# src/domain/metadata/blueprint/structure/register/square/blueprint.py

"""
Module: domain.metadata.blueprint.structure.register.square.blueprint.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain.metadata.blueprint.structure import RegisterBlueprint
from err import RegisterNullException, SquareRegisterNullException
from domain.model import Square
from domain.structure.searchable.register import SquareRegister


class SquareRegisterBlueprint(RegisterBlueprint[SquareRegister]):
    """
    Role:
        - Container

    Responsibilities:
        1.  Provides values for hydrating a SquareRegister object.

    Attributes:
        origin: Square
        destination: Square
        domain_class: Type[SquareRegister]
        domain_null_exception: Optional[SquareRegisterNullException]

    Provides:

    Super Class:
        RegisterBlueprint
    """
    
    def __init__(
            self,
            origin: Square,
            destination: Square,
            domain_class: Type[SquareRegister] = SquareRegister,
            domain_null_exception: Optional[SquareRegisterNullException] |
                            None = SquareRegisterNullException(),
    ):
        """
        Args:
            origin: Square
            destination: Square
            domain_class: Type[SquareRegister]
            domain_null_exception: Optional[SquareRegisterNullException]
        """
        super().__init__(
            a=origin,
            b=destination,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception,
        )
    
    @property
    def domain_class(self) -> Type[SquareRegister]:
        return cast(Type[SquareRegister], super().domain_class)
    
    @property
    def origin(self) -> Square:
        return cast(Square, self.a)
    
    @property
    def destination(self) -> Square:
        return cast(Square, self.b)
    
    @property
    def a(self) -> Square:
        return cast(Square, self.a)
    
    @property
    def b(self) -> Square:
        return cast(Square, self.b)
    
    @property
    def domain_null_exception(self) -> RegisterNullException:
        return cast(SquareRegisterNullException, super().domain_null_exception)
