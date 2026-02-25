# src/chess/square/service/operation/operation.py

"""
Module: chess.square.service.operation.operation
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, Dict

from chess.board import Board
from chess.coord import Coord
from chess.square import SquareServiceOperation


class SquareBuildOperation(SquareServiceOperation):
    """
    A class representing a service operation.
    """
    
    NAME = "build_square"
    PARAMETERS = Dict[
        "id": int,
        "name" : str,
        "board": Board,
        "coord": Coord,
    ]
    
    def __init__(
            self,
            name: str = NAME,
            parameters: Dict[str, Any] = PARAMETERS
    ):
        super().__init__(name=name, parameters=parameters)

    @classmethod
    def key(cls) -> SquareBuildOperation:
        return cls.__init__(name=cls.NAME, parameters=cls.PARAMETERS)