# src/domain/search/model/square/context.py

"""
Module: domain.search.model.square.comtext
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Board, Coord, SquareState, ModelContext, Square, SquareType, Token


class SquareContext(ModelContext[Square]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply SquareSearcher with targeting criteria.

    Attributes:
        id: Optional[int]
        name: Optional[str]
        board: Optional[Board]
        coord: Optional[Coord]
        occupant: Optional[Token]
        state: Optional[SquareState]
        square_type: Optional[SquareType]
            
    Provides:
        -  to_dict() -> Dict[str, Any]

    Super Class:
        ModelContext
    """
    _board: Optional[Board]
    _coord: Optional[Coord]
    _occupant: Optional[Token]
    _state: Optional[SquareState]
    _square_type: Optional[SquareType]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            board: Optional[Board] | None = None,
            coord: Optional[Coord] | None = None,
            occupant: Optional[Token] | None = None,
            state: Optional[SquareState] | None = None,
            square_type: Optional[SquareType] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
            board: Optional[Board]
            coord: Optional[Coord]
            occupant: Optional[Token]
            state: Optional[SquareState]
            square_type: Optional[SquareType]
        """
        super().__init__(id=id, name=name)
        self._board = board
        self._coord = coord
        self._state = state
        self._occupant = occupant
        self._square_type = square_type
    
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
    def square_type(self) -> Optional[SquareType]:
        return self._square_type
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "board": self._board,
            "coord": self._coord,
            "state": self._state,
            "occupant": self._occupant,
            "square_type": self._square_type,
        }