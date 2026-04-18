# src/model/square/opening/model.py

"""
Module: model.square.opening/model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Coord, Formation, Square
from model.board import Board



class OpeningSquare(Square):
    _formation: Formation
    
    def __init__(
            self,
            id: int,
            name: str,
            coord: Coord,
            board: Board,
            formation: Formation,
    ):
        """
        Args:
            id: int
            name: str
            board: Board
            coord: Coord
            formation: Formation
        """
        super().__init__(id=id, name=name, coord=coord, board=board)
        self._formation = formation
    
    @property
    def formation(self) -> Formation:
        return self._formation
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Square):
            return self._id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
