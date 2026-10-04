# src/domain/metadata/blueprint/struct/register/vector.blueprint.py

"""
Module: domain.metadata.blueprint.struct.register.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import RegisterBlueprint, Vector, VectorRegister
from err import VectorRegisterNullException


class VectorRegisterBlueprint(RegisterBlueprint[VectorRegister]):
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

     Provides:

     Super Class:
        RegisterBlueprint
     """
    _u: Vector
    _v: Vector
    
    def __init__(
            self,
            u: Vector,
            v: Vector,
            domain_class: Optional[Type[VectorRegister]] | None = None,
            domain_null_exception: Optional[VectorRegisterNullException] | None = None,
    ):
        """
        Args:
            u: Vector
            v: Vector
            domain_class: Optional[Type[VectorRegister]]
            domain_null_exception: Optional[VectorRegisterNullException]
        """
        super().__init__(
            domain_class=domain_class or VectorRegister,
            domain_null_exception=domain_null_exception or VectorRegisterNullException(),
        )
        self._u = u
        self._v = v
        
    @property
    def u(self) -> Vector:
        return self._u
    
    @property
    def v(self) -> Vector:
        return self._v
    
    @property
    def domain_class(self) -> Type[VectorRegister]:
        return cast(Type[VectorRegister], super().domain_class)
    
    @property
    def domain_null_exception(self) -> VectorRegisterNullException:
        return cast(VectorRegisterNullException, super().domain_null_exception)
    
    
