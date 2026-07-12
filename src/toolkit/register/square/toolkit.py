# src/toolkit/register/square/.py

"""
Module: toolkit.register.square.
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import SquareRegisterBlueprint
from err import SquareRegisterNullException
from  import Square, SquareRegister
from toolkit import RegisterToolkit
from validator import SquareValidator


class SquareRegisterToolkit(RegisterToolkit[Square]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for SquareRegister tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        square_validator: SquareValidator
        null_exception: SquareRegisterNullException
        : SquareRegister

    Provides:

    Super Class:
       RegisterToolkit
    """
    a: Square
    b: Square
    square_validator: SquareValidator = SquareValidator()
    null_exception = SquareRegisterNullException = SquareRegisterNullException()
    : SquareRegister = Type[SquareRegister]
    blueprint_: SquareRegisterBlueprint = Type[SquareRegisterBlueprint]
    
    
    @property
    def origin(self) -> Square:
        return cast(Square, self.a)
    
    @property
    def destination(self) -> Square:
        return cast(Square, self.b)
    
