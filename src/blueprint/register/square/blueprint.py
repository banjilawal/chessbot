# src/blueprint/register/square/blueprint.py

"""
Module: blueprint.register.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from blueprint import RegisterBlueprint
from err import RegisterNullException, SquareRegisterNullException
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
        model_class: Type[SquareRegister]
        null_exception: Optional[SquareRegisterNullException]

    Provides:

    Super Class:
        RegisterBlueprint
    """
    
    def __init__(
            self,
            origin: Square,
            destination: Square,
            model_class: Type[SquareRegister] = SquareRegister,
            null_exception: Optional[SquareRegisterNullException] |
                            None = SquareRegisterNullException(),
    ):
        """
        Args:
            origin: Square
            destination: Square
            model_class: Type[SquareRegister]
            null_exception: Optional[SquareRegisterNullException]
        """
        super().__init__(
            a=origin,
            b=destination,
            model_class=model_class,
            null_exception=null_exception,
        )
    
    @property
    def model_class(self) -> Type[SquareRegister]:
        return cast(Type[SquareRegister], super().model_class)
    
    @property
    def origin(self) -> Square:
        return cast(Square, self.a)
    
    @property
    def destination(self) -> Square:
        return cast(Square, self.b)
    
    @property
    def a(self) -> Square:
        return cast(Square, self.a)
    
    @property
    def b(self) -> Square:
        return cast(Square, self.b)
    
    @property
    def null_exception(self) -> RegisterNullException:
        return cast(SquareRegisterNullException, super().null_exception)
