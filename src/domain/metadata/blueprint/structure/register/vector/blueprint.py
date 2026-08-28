# src/domain/metadata/blueprint/structure/register/vector/blueprint.py

"""
Module: domain.metadata.blueprint.structure.register.vector.blueprint.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain.metadata.blueprint.structure import RegisterBlueprint
from err import RegisterNullException, VectorRegisterNullException
from domain.model import Vector
from domain.structure.register import VectorRegister


class VectorRegisterBlueprint(RegisterBlueprint[VectorRegister]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a VectorRegister object.

    Attributes:
        u: Vector
        v: Vector
        domain_class: Type[VectorRegister]
        domain_null_exception: Optional[VectorRegisterNullException]

    Provides:

    Super Class:
        RegisterBlueprint
    """
    
    def __init__(
            self,
            u: Vector,
            v: Vector,
            domain_class: Type[VectorRegister] = VectorRegister,
            domain_null_exception: Optional[VectorRegisterNullException] |
                            None = VectorRegisterNullException(),
    ):
        """
        Args:
            u: Vector
            v: Vector
            domain_class: Type[VectorRegister]
            domain_null_exception: Optional[VectorRegisterNullException]
        """
        super().__init__(
            a=u,
            b=v,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception,
        )
    
    @property
    def domain_class(self) -> Type[VectorRegister]:
        return cast(Type[VectorRegister], super().domain_class)
    
    @property
    def u(self) -> Vector:
        return cast(Vector, super().a)
    
    @property
    def v(self) -> Vector:
        return cast(Vector, super().b)
    
    @property
    def a(self) -> Vector:
        return self.u
    
    @property
    def b(self) -> Vector:
        return self.v
    
    @property
    def domain_null_exception(self) -> RegisterNullException:
        return cast(VectorRegisterNullException, super().domain_null_exception)
    #
    # @property
    # def is_empty(self) -> bool:
    #     return self.size == 0
    #
    # @property
    # def is_right_size(self) -> bool:
    #     return self.size == 2
    #
    # @property
    # def is_wrong_size(self) -> bool:
    #     return not (
    #             self.is_empty and self.is_right_size
    #     )
    #
    # @property
    # def size(self) -> int:
    #     return len([self.a, self.b])
    #
    # @property
    # def registers_are_same_type(self) -> bool:
    #     return isinstance(self.u, type(self.v))
    #
    # @property
    # def registers_have_different_types(self) -> bool:
    #     return not self.registers_are_same_type
