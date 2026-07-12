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
from register import Register


class RegisterBlueprint(Blueprint[Register]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a B object.

    Attributes:
        a: Any
        b: Any
        model_type: Type[Register]

    Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(self, a: Any, b: Any, model_class: Type[Register]):
        """
        Args:
            a: Any
            b: Any
            model_class: Type[Register]
        """
        super().__init__(model_class=model_class)
        self._a = a
        self._b = b
    
    @property
    def mode_class(self) -> Type[Register]:
        return cast(Type[Register], self.model_class)
    
    @property
    def a(self) -> Any:
        return self._a
    
    @property
    def b(self) -> Any:
        return self._b
