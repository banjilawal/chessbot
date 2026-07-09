# src/blueprint/model/square/blueprint.py

"""
Module: blueprint.model.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Type

from blueprint import Blueprint
from err import SquareNullException
from model import Board, Coord, Square
from schema import Formation


@dataclass
class SquareBlueprint(Blueprint[Square]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Square object.

    Attributes:
        name: str
        board: Board
        coord: Coord
        id: Optional[int]
        formation: Optional[Formation]
        null_exception: SquareNullException
        model_type: Square
        
    Provides:

     Super Class:
        Blueprint
     """
    """
    Args:
        name: str
        board: Board
        coord: Coord
        id: Optional[int]
        formation: Optional[Formation]
        null_exception: SquareNullException
        owner: Square
        owner_name: str
    """
    name: str
    board: Board
    coord: Coord
    id: Optional[int] | None = None
    formation: Optional[Formation] | None = None
    null_exception: SquareNullException = SquareNullException()
    owner: Square = Type[Square]
    owner_name: str = type(owner).__name__