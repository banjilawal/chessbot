# src/chess/square/map.py

"""
Module: chess.square.map
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import Optional

from chess.board import Board
from chess.coord import Coord
from chess.square import Square
from chess.system import Context


class SquareContext(Context[Square]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    Provide an SquareFinder with an attribute value to find Squares with a matching value in
    their version of the attribute.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   board (Optional[Board])
        *   coord (Optional[Coord])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _board: Optional[Board]
    _coord: Optional[Coord]
    
    def __init__(
            self,
            id: Optional[int],
            name: Optional[str],
            board: Optional[Board] = None,
            coord: Optional[Coord] = None
    ):
        super().__init__(id=id, name=name)
        self._board = board
        self._coord = coord
        
    @property
    def board(self) -> Optional[Board]:
        return self._board
        
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    def to_dict(self) -> dict:
        """
        # ACTION:
        Convert a SquareContext attributes into a dictionary.
        # PARAMETERS:
        None
        # RETURNS:
            dict
        # RAISES:
        None
        """
        return {
            "id": self.id,
            "name": self.name,
            "board": self._board,
            "coord": self._coord,
        }