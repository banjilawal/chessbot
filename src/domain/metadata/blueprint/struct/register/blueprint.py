# src/domain/metadata/blueprint/struct/register/blueprint.py

"""
Module: domain.metadata.blueprint.struct.register.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Type, TypeVar, cast

from domain import Model, Register, StructBlueprint
from err import RegisterNullException

T = TypeVar("T", bound="Register")
M = TypeVar("M", bound="Model")


class RegisterBlueprint(StructBlueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Register.

     Attributes:
        a: Any
        b: Any
        domain_class: Type[T]
        domain_null_exception: RegisterNullException

     ProvideT:

     Super class:
        StructBlueprint
     """
    _a: Any
    _b: Any
    
    def __init__(
            self,
            a: Any,
            b: Any,
            domain_class: Type[T],
            domain_null_exception: RegisterNullException,
    ):
        """
        ArgT:
            a: Any
            b: Any
            domain_class: Type[T]
            domain_null_exception: RegisterNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
        self._a = a
        self._b = b
    
    @property
    def a(self) -> M:
        return self._a
    
    @property
    def b(self) -> M:
        return self._b
    
    @property
    @abstractmethod
    def a_is_b(self) -> bool:
        pass
    
    @property
    def a_is_not_b(self) -> bool:
        return not self.a_is_b
    
    @property
    def size(self) -> int:
        return len(self.to_dict)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def is_balanced(self) -> bool:
        return self.size == 2
    
    @property
    def is_not_balanced(self) -> bool:
        return self.size == 1
    
    @property
    def consistency_exists(self) -> bool:
        if (
                self is None or
                self.is_empty or
                self.is_not_balanced
        ):
            return False
        return True
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {"a": self._a, "b": self._b}
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> RegisterNullException:
        return cast(RegisterNullException, super().domain_null_exception)

    
