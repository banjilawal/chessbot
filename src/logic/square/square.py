# src/logic/square/item.py

"""
Module: logic.square.item
Author: Banji Lawal
Created: 2025-07-26
"""

from __future__ import annotations
from typing import Optional

from logic.board import Board
from logic.coord import Coord
from logic.token import Token
from logic.square.state import SquareState


class Square:
    """
    # ROLE: Data-Holder, Addressing, Referencing

    # RESPONSIBILITIES:
    1.  Maps a Coord to a nameable, occupyable board location.
    2.  Space on Board a Token can occupy.
    3.  Metadata about a reference on the Board.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   board (Board)
        *   coord (Coord)
       *    state (SquareState)
       *    occupant (Optional[Token])

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
        *   id (int)
        *   name (str)
        *   board (Board)
        *   coord (Coord)
        *   state (SquareState)

    # LOCAL METHODS:
        *   is_empty(self) -> bool
        *   is_occupied(self) -> bool

    # INHERITED METHODS:
    None
    """
    _id: int
    _name: str
    _board: Board
    _coord: Coord
    _state: SquareState
    _occupant: Optional[Token]
    
    def __init__(self, id: int, name: str, coord: Coord, board: Board):
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
    def is_occupied(self) -> bool:
        return self._occupant is not None and self._state != SquareState.EMPTY
    
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
