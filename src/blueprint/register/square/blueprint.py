# src/blueprint/register/square/blueprint.py

"""
Module: blueprint.register.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import RegisterBlueprint
from model import Square
from register import SquareRegister


class SquareRegisterBlueprint(RegisterBlueprint[SquareRegister]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a SquareRegister object.

    Attributes:
        origin: Square
        destination: Square

    Provides:

    Super Class:
        RegisterBlueprint
    """
    
    def __init__(
            self,
            origin: Square,
            destination: Square,
            model_class: Type[SquareRegister] = SquareRegister,
    ):
        """
        Args:
            origin: Square
            destination: Square
            model_class: Type[SquareRegister]
        """
        super().__init__(a=origin, b=destination, model_class=model_class)
    
    @property
    def mode_class(self) -> Type[SquareRegister]:
        return cast(Type[SquareRegister], self.model_class)
    
    @property
    def origin(self) -> Square:
        return cast(Square, self.a)
    
    @property
    def destination(self) -> Square:
        return cast(Square, self.b)
