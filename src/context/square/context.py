# src/context/square/model/state.py

"""
Module: context.square.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from context import Context
from model import Square


class SquareContext(Context[Square]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Square attribute-value search filter.

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
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            board: Optional[Board] | None = None,
            coord: Optional[Coord] | None = None,
            occupant: Optional[Token] | None = None,
            state: Optional[SquareState] | None = None,
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
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "board": self.board,
            "coord": self.coord,
            "occupant": self.occupant,
            "state": self.state,
        }