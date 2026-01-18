# src/chess/square/square.py

"""
Module: chess.square.square
Author: Banji Lawal
Created: 2025-07-26
"""

from typing import Optional

from chess.board import Board
from chess.coord import Coord
from chess.square.state import SquareState
from chess.token import Token


class Square:
    """
    # ROLE: Data-Holding, Addressing
  
    # RESPONSIBILITIES:
    1.  Maps a Coord to its unique name.
    2.  Space a Token occupies on the Board.
    
    # PARENT:
    None
    
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
        *   _name (str)
        *   _board (Board)
        *   _coord (Coord)
        *   _occupant (Optional[Token])
        
    # INHERITED ATTRIBUTES:
    None
    """
    _id: int
    _name: str
    _board: Board
    _coord: Coord
    _state: SquareState
    _occupant: Optional[Token]
    
    def __init__(self, id: int, name: str, coord: Coord, board: Board):
        """
        # ACTION:
            Constructor.
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   coord (Coord)
            *   board (Board)
        # RETURNS:
            Non
        # RAISES:
            None
        """
        self._id = id
        self._name = name
        self._coord = coord
        self._board = board
        self._occupant = None
        self._state = SquareState.EMPTY
    
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
    def is_empty(self) -> bool:
        return self._state == SquareState.EMPTY and self._occupant is None
    
    @property
    def state(self) -> SquareState:
        return self._state
    
    @state.setter
    def state(self, state: SquareState):
        self._state = state
    
    @property
    def occupant(self) -> Optional[Token]:
        return self._occupant
    
    @occupant.setter
    def occupant(self, token: Optional[Token]):
        self._occupant = token
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Square):
            return self._id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
    
    # def __str__(self) -> str:
    #     occupant_str = f" occupant:{self._occupant.name}" if self._occupant else ""
    #     return f"Square:[{self._id} {self._name} {self._coord}{occupant_str}]"
