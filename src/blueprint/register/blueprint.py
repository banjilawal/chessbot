# src/blueprint/register/blueprint.py

"""
Module: blueprint.register.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from blueprint import Blueprint
from err import RegisterNullException
from register import Register


class RegisterBlueprint(Blueprint[Register]):
    """
    Role:
    -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a Register object.
    
    Attributes:
        a: Any
        b: Any
        model_type: Type[Register]
        null_exception: RegisterNullException
    
    Provides:
    
    Super Class:
        Blueprint
    """
    
    def __init__(
            self,
            a: Any,
            b: Any,
            model_class: Type[Register] = Register,
            null_exception: RegisterNullException | None = RegisterNullException(),
    ):
        """
        Args:
            a: Any
            b: Any
            model_class: Type[Register]
            null_exception: RegisterNullException
        """
        super().__init__(model_class=model_class, null_exception=null_exception)
        self._a = a
        self._b = b
        
    
    @property
    def model_class(self) -> Type[Register]:
        return cast(Type[Register], super().model_class)
    
    @property
    def null_exception(self) -> RegisterNullException:
        return cast(RegisterNullException, super().null_exception)
    
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
    
