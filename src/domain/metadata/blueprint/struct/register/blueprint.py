# src/domain/struct/register/blueprint.py

"""
Module: domain.struct.register.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Type, TypeVar, cast

from domain import Model, Register, StructBlueprint
from err import RegisterNullException

S = TypeVar("S", bound="Register")
M = TypeVar("M", bound="Model")


class RegisterBlueprint(StructBlueprint[S, M], ABC, Generic[S, M]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Register.

     Attributes:
        a: M
        b: M
        domain_class: Type[S]
        domain_null_exception: RegisterNullException

     Provides:

     Super Class:
        StructBlueprint
     """
    _a: M
    _b: M
    
    def __init__(
            self,
            a: M,
            b: M,
            domain_class: Type[S],
            domain_null_exception: RegisterNullException,
    ):
        """
        Args:
            a: M
            b: M
            domain_class: Type[S]
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
    def to_dict(self) -> Dict[str, M]:
        return {"a": self._a, "b": self._b}
    
    @property
    def domain_class(self) -> Type[S]:
        return cast(Type[S], super().domain_class)
    
    @property
    def domain_null_exception(self) -> RegisterNullException:
        return cast(RegisterNullException, super().domain_null_exception)

    
