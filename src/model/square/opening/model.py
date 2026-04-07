# src/model/square/opening/model.py

"""
Module: model.square.opening/model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import Formation, Square
from model.board import Board
from model.coord import Coord
from model.token import Token
from model.model.state import SquareState


class OpeningSquare(Square):
    _formation: Formation
    
    def __init__(
            self,
            id: int,
            name: str,
            coord: Coord,
            board: Board,
    ):
        """
        Args:
            id: int
            name: str
            board: Board
            coord: Coord
            state: SquareState
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
