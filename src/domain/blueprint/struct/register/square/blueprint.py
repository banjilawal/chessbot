# src/domain/bluprint/struct/register/square.blueprint.py

"""
Module: domain.bluprint.struct.register.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, Type, cast

from domain import RegisterBlueprint, Square, SquareRegister
from err import SquareRegisterNullException


class SquareRegisterBlueprint(RegisterBlueprint[SquareRegister, Square]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a SquareRegister.

     Attributes:
        u: Square
        v: Square
        domain_class: Optional[Type[SquareRegister]]
        domain_null_exception: Optional[SquareRegisterNullException]

     ProvideT:

     Super class:
        RegisterBlueprint
     """
    
    def __init__(
            self,
            u: Square,
            v: Square,
            domain_class: Optional[Type[SquareRegister]] | None = None,
            domain_null_exception: Optional[SquareRegisterNullException] | None = None,
    ):
        """
        ArgT:
            u: Square
            v: Square
            domain_class: Optional[Type[SquareRegister]]
            domain_null_exception: Optional[SquareRegisterNullException]
        """
        super().__init__(
            a=u,
            b=v,
            domain_class=domain_class or SquareRegister,
            domain_null_exception=domain_null_exception or SquareRegisterNullException(),
        )
    
    @property
    def u(self) -> Square:
        return cast(Square, super().a)
    
    @property
    def a(self) -> Square:
        return self.u
    
    @property
    def v(self) -> Square:
        return cast(Square, super().b)
    
    @property
    def b(self) -> Square:
        return self.v
    
    @property
    def u_is_v(self) -> bool:
        return self.u == self.v
    
    @property
    def u_is_not_v(self) -> bool:
        return not self.u_is_v
    
    @property
    def a_is_b(self) -> bool:
        return self.u_is_v
    
    @property
    def to_dict(self) -> Dict[str, Square]:
        return {
            "u": self.u,
            "v": self.v,
        }
    
    @property
    def domain_class(self) -> Type[SquareRegister]:
        return cast(Type[SquareRegister], super().domain_class)
    
    @property
    def domain_null_exception(self) -> SquareRegisterNullException:
        return cast(SquareRegisterNullException, super().domain_null_exception)

    
