# src/domain/metadata/blueprint/struct/register/coord.blueprint.py

"""
Module: domain.metadata.blueprint.struct.register.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, Type, cast

from domain import RegisterBlueprint, Coord, CoordRegister
from err import CoordRegisterNullException


class CoordRegisterBlueprint(RegisterBlueprint[CoordRegister, Coord]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a CoordRegister.

     Attributes:
        u: Coord
        v: Coord
        domain_class: Optional[Type[CoordRegister]]
        domain_null_exception: Optional[CoordRegisterNullException]

     ProvideT:

     Super class:
        RegisterBlueprint
     """
    
    def __init__(
            self,
            u: Coord,
            v: Coord,
            domain_class: Optional[Type[CoordRegister]] | None = None,
            domain_null_exception: Optional[CoordRegisterNullException] | None = None,
    ):
        """
        ArgT:
            u: Coord
            v: Coord
            domain_class: Optional[Type[CoordRegister]]
            domain_null_exception: Optional[CoordRegisterNullException]
        """
        super().__init__(
            a=u,
            b=v,
            domain_class=domain_class or CoordRegister,
            domain_null_exception=domain_null_exception or CoordRegisterNullException(),
        )
    
    @property
    def u(self) -> Coord:
        return cast(Coord, super().a)
    
    @property
    def a(self) -> Coord:
        return self.u
    
    @property
    def v(self) -> Coord:
        return cast(Coord, super().b)
    
    @property
    def b(self) -> Coord:
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
    def to_dict(self) -> Dict[str, Coord]:
        return {
            "u": self.u,
            "v": self.v,
        }
    
    @property
    def domain_class(self) -> Type[CoordRegister]:
        return cast(Type[CoordRegister], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CoordRegisterNullException:
        return cast(CoordRegisterNullException, super().domain_null_exception)

    
