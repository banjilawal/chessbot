# src/blueprint/model/register/square/blueprint.py

"""
Module: blueprint.model.register.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import Blueprint
from err import SquareRegisterNullException
from model import Square, SquareRegister



@dataclass
class SquareRegisterBlueprint(Blueprint[SquareRegister]):
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
    """
    Args:
        origin: Square
        destination: Square
        null_exception: SquareRegisterNullException
        owner: SquareRegister
        owner_name: str
    """
    origin: Square
    destination: Square
    null_exception: SquareRegisterNullException = SquareRegisterNullException()
    owner: SquareRegister = Type[SquareRegister]
    owner_name: str = type(owner).__name__
