# src/blueprint/model/register/square/blueprint.py

"""
Module: blueprint.model.register.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type, cast

from blueprint import RegisterBlueprint
from err import SquareRegisterNullException
from model import Square, SquareRegister



@dataclass
class SquareRegisterBlueprint(RegisterBlueprint[SquareRegister]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a SquareRegister object.

    Attributes:
        origin: Square
        destination: Square
        null_exception: SquareRegisterNullException
        owner: SquareRegister
        owner_name: str
            
    Provides:

     Super Class:
        Blueprint
     """

    # a: Square
    # b: Square
    # null_exception: SquareRegisterNullException = SquareRegisterNullException()
    # owner: SquareRegister = Type[SquareRegister]
    # owner_name: str = type(owner).__name__
    
    def __init__(
            self,
            origin: Square,
            destination: Square,
            null_exception: SquareRegisterNullException | None = SquareRegisterNullException(),
            owner: SquareRegister | None = Type[SquareRegister],
            owner_name: str | None = type(SquareRegister).__name__,
    ):
        """
        Args:
            origin: Square
            destination: Square
            null_exception: SquareRegisterNullException
            owner: SquareRegister
            owner_name: str
        """
        super().__init__(
            a=origin,
            b=destination,
            owner=owner,
            null_exception=null_exception,
            owner_name=owner_name,
        )
    
    @property
    def origin(self) -> Square:
        return cast(Square, self.a)
    
    @property
    def destination(self) -> Square:
        return cast(Square, self.b)
    
    @property
    def model(self):
        return Type[SquareRegister]
    
    @property
    def null_exception(self) -> SquareRegisterNullException:
        return SquareRegisterNullException()
