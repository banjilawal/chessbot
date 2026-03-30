# src/logic/square/query/context/context/model.py

"""
Module: logic.square.query.context.context.context
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from logic.board import Board
from logic.coord import Coord
from logic.square import Square

from logic.square.model.state import SquareState
from logic.system import Context
from logic.token import Token


class SquareContext(Context[Square]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply Square related workers with execution routing information where:
                -   Square.attribute: execution path selector (routing key).
                -   attribute.value: executor input.

    Attributes:
        id: Optional[int]
        name: Optional[str]
        board: Optional[Board]
        coord: Optional[Coord]
        occupant: Optional[Token]
        state: Optional[SquareState]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    _board: Optional[Board]
    _coord: Optional[Coord]
    _occupant: Optional[Token]
    _state: Optional[SquareState]
    
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            board: Optional[Board] = None,
            coord: Optional[Coord] = None,
            occupant: Optional[Token] = None,
            state: Optional[SquareState] = None,
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
            board: Optional[Board]
            coord: Optional[Coord]
            occupant: Optional[Token]
            state: Optional[SquareState]
        """
        super().__init__(id=id, name=name)
        self._board = board
        self._coord = coord
        self._occupant = occupant
        self._state = state
        
    @property
    def board(self) -> Optional[Board]:
        return self._board
        
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    @property
    def occupant(self) -> Optional[Token]:
        return self._occupant
    
    @property
    def state(self) -> Optional[SquareState]:
        return self._state
    
    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the SquareContext.
        """
        return {
            "id": self.id,
            "name": self.name,
            "board": self._board,
            "coord": self._coord,
            "occupant": self._occupant,
            "state": self._state,
        }