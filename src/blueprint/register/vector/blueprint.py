# src/blueprint/register/vector/blueprint.py

"""
Module: blueprint.register.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from blueprint import RegisterBlueprint
from err import RegisterNullException, VectorRegisterNullException
from model import Vector
from register import VectorRegister


class VectorRegisterBlueprint(RegisterBlueprint[VectorRegister]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a VectorRegister object.

    Attributes:
        u: Vector
        v: Vector
        model_class: Type[VectorRegister]
        null_exception: Optional[VectorRegisterNullException]

    Provides:

    Super Class:
        RegisterBlueprint
    """
    
    def __init__(
            self,
            u: Vector,
            v: Vector,
            model_class: Type[VectorRegister] = VectorRegister,
            null_exception: Optional[VectorRegisterNullException] |
                            None = VectorRegisterNullException(),
    ):
        """
        Args:
            u: Vector
            v: Vector
            model_class: Type[VectorRegister]
            null_exception: Optional[VectorRegisterNullException]
        """
        super().__init__(
            a=u,
            b=v,
            model_class=model_class,
            null_exception=null_exception,
        )
    
    @property
    def model_class(self) -> Type[VectorRegister]:
        return cast(Type[VectorRegister], super().model_class)
    
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
    def null_exception(self) -> RegisterNullException:
        return cast(VectorRegisterNullException, super().null_exception)
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
