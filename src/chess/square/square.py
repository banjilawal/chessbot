# src/chess/square/square.py

"""
Module: chess.square.square
Author: Banji Lawal
Created: 2025-07-26
"""

from typing import Optional

from chess.board import Board
from chess.coord import Coord
from chess.piece import Piece


class Square:
    """
    # ROLE: Data-Holding
  
    # RESPONSIBILITIES:
    1.  A Piece occupies a Square.
    2.  Provides reference to a Piece.
    
    # PROVIDES:
    Square
  
    # ATTRIBUTES:
        *   timestamp (int)
        *   _name (str)
        *   _board (Board)
        *   _coord (Coord)
        *   _occupant (Optional[Piece])
    """
    _id: int
    _name: str
    _board: Board
    _coord: Coord
    _occupant: Optional[Piece]
    
    def __init__(self, id: int, name: str, coord: Coord, board: Board):
        """
        # ACTION:
        Construct a Piece instance.
        
        # PARAMETERS:
            *   id (int)
            *   designation (str)
            *   target (Coord)
        
        # Returns:
        None
        
        # RAISES:
        None
        """
        self._id = id
        self._name = name
        self._coord = coord
        self._board = board
        self._occupant = None
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def coord(self) -> Coord:
        return self._coord
    
    @property
    def occupant(self) -> Optional[Piece]:
        return self._occupant
    
    @occupant.setter
    def occupant(self, piece: Optional[Piece]):
        self._occupant = piece
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Square):
            return self._id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:
        occupant_str = f" occupant:{self._occupant.name}" if self._occupant else ""
        return f"Square:[{self._id} {self._name} {self._coord}{occupant_str}]"
