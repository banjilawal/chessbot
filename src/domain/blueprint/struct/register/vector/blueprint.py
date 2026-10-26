# src/domain/bluprint/struct/register/vector.blueprint.py

"""
Module: domain.bluprint.struct.register.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, Type, cast

from domain import RegisterBlueprint, Vector, VectorRegister
from err import VectorRegisterNullException


class VectorRegisterBlueprint(RegisterBlueprint[VectorRegister, Vector]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a VectorRegister.

     Attributes:
        u: Vector
        v: Vector
        domain_class: Optional[Type[VectorRegister]]
        domain_null_exception: Optional[VectorRegisterNullException]

     ProvideT:

     Super class:
        RegisterBlueprint
     """
    
    def __init__(
            self,
            u: Vector,
            v: Vector,
            domain_class: Optional[Type[VectorRegister]] | None = None,
            domain_null_exception: Optional[VectorRegisterNullException] | None = None,
    ):
        """
        ArgT:
            u: Vector
            v: Vector
            domain_class: Optional[Type[VectorRegister]]
            domain_null_exception: Optional[VectorRegisterNullException]
        """
        super().__init__(
            a=u,
            b=v,
            domain_class=domain_class or VectorRegister,
            domain_null_exception=domain_null_exception or VectorRegisterNullException(),
        )
    
    @property
    def u(self) -> Vector:
        return cast(Vector, super().a)
    
    @property
    def a(self) -> Vector:
        return self.u
    
    @property
    def v(self) -> Vector:
        return cast(Vector, super().b)
    
    @property
    def b(self) -> Vector:
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
    def to_dict(self) -> Dict[str, Vector]:
        return {
            "u": self.u,
            "v": self.v,
        }
    
    @property
    def domain_class(self) -> Type[VectorRegister]:
        return cast(Type[VectorRegister], super().domain_class)
    
    @property
    def domain_null_exception(self) -> VectorRegisterNullException:
        return cast(VectorRegisterNullException, super().domain_null_exception)

    
