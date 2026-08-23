# src/domain/search/context/stack/square/context.py

"""
Module: domain.search.context.stack.square.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Board, Coord, SquareState, StackSearchContext, Square, Token


class SquareSearchContext(StackSearchContext[Square]):
    """
    Role:
        -   Selection
        -   Routing mask

    Responsibilities:
        1.  Supply the criteria a SquareStackSearcher uses to find a hit.

    Attributes:
        id: Optional[int]
        name: Optional[str]
        board: Optional[Board]
        coord: Optional[Coord]
        occupant: Optional[Token]
        state: Optional[SquareState]
        home_square_type: Optional[bool]
            
    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        StackSearchContext
    """
    _board: Optional[Board]
    _coord: Optional[Coord]
    _occupant: Optional[Token]
    _state: Optional[SquareState]
    _home_square_type: Optional[bool]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            board: Optional[Board] | None = None,
            coord: Optional[Coord] | None = None,
            occupant: Optional[Token] | None = None,
            state: Optional[SquareState] | None = None,
            home_square_type: Optional[bool] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
            board: Optional[Board]
            coord: Optional[Coord]
            occupant: Optional[Token]
            state: Optional[SquareState]
            home_square_type: Optional[bool]
        """
        super().__init__(id=id, name=name)
        self._board = board
        self._coord = coord
        self._occupant = occupant
        self._state = state
        self._home_square_type = home_square_type
    
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
    def home_square_type(self) -> Optional[bool]:
        return self._home_square_type
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "board": self.board,
            "coord": self.coord,
            "occupant": self.occupant,
            "state": self.state,
            "home_square_type": self.home_square_type,
        }