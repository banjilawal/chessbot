# src/blueprint/square/model.py

"""
Module: blueprint.square.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import SquareNullException
from model import Blueprint, Board, Coord, Formation, Square

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
    name: str
    board: Board
    coord: Coord
    id: Optional[int] | None = None
    formation: Optional[Formation] | None = None
    null_exception: SquareNullException = SquareNullException()
    model_type: Square = Square