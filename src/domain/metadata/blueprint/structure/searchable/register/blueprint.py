# src/domain/metadata/blueprint/structure/register/blueprint.py

"""
Module: domain.metadata.blueprint.structure.register.blueprint.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Generic, List, Type, TypeVar, cast

from domain.metadata.blueprint.structure import Blueprint
from err import RegisterNullException
from domain.structure.searchable.register import Register

T = TypeVar("T", bound="Register")


class RegisterBlueprint(Blueprint, Generic[T]):
    """
    Role:
    -  Container
    
    Responsibilities:
        1.  Provides values for hydrating a Register object.
    
    Attributes:
        a: Any
        b: Any
        model_type: Type[Register]
        domain_null_exception: RegisterNullException
    
    Provides:
    
    Super Class:
        Blueprint
    """
    
    def __init__(
            self,
            a: Any,
            b: Any,
            domain_class: Type[Register] = Register,
            domain_null_exception: RegisterNullException | None = RegisterNullException(),
    ):
        """
        Args:
            a: Any
            b: Any
            domain_class: Type[Register]
            domain_null_exception: RegisterNullException
        """
        super().__init__(domain_class=domain_class, domain_null_exception=domain_null_exception)
        self._a = a
        self._b = b
        
    
    @property
    def domain_class(self) -> Type[Register]:
        return cast(Type[Register], super().domain_class)
    
    @property
    def domain_null_exception(self) -> RegisterNullException:
        return cast(RegisterNullException, super().domain_null_exception)
    
    @property
    def a(self) -> Any:
        return self._a
    
    @property
    def b(self) -> Any:
        return self._b
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_right_size(self) -> bool:
        return self.size == 2
    
    @property
    def is_wrong_size(self) -> bool:
        return not (
                self.is_empty and self.is_right_size
        )
    
    @property
    def size(self) -> int:
        return len([self._a, self._b])
    
    @property
    def registers_are_same_type(self) -> bool:
        return isinstance(self._a, type(self._b))
    
    @property
    def registers_have_different_types(self) -> bool:
        return not self.registers_are_same_type
    
    @property
    def to_list(self) -> List[T]:
        return [self._a, self._b]
    
