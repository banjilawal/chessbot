# src/model/context/square/model.py

"""
Module: model.context.square.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional

from model import Board, Context, Coord, Square, SquareState, Token


class SquareContext(Context[Square]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Square attribute-value tuple which selects an execution path.

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
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "board": self._board,
            "coord": self._coord,
            "occupant": self._occupant,
            "state": self._state,
        }