# src/logic/edge/map.py

"""
Module: logic.edge.map
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from logic.board import Board
from logic.coord import Coord
from logic.edge import Edge


from logic.edge.state import EdgeState
from logic.system import Context
from logic.token import Token


class EdgeContext(Context[Edge]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    Provide an EdgeFinder with an attribute value to find Edges with a matching value in teir version of
    the attribute.

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
    _occupant: Optional[Token]
    _state: Optional[EdgeState]
    
    def __init__(
            self,
            id: Optional[int],
            name: Optional[str],
            board: Optional[Board] = None,
            coord: Optional[Coord] = None,
            occupant: Optional[Token] = None,
            state: Optional[EdgeState] = None,
    ):
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
    def state(self) -> Optional[EdgeState]:
        return self._state
    
    def to_dict(self) -> dict:
        """
        # ACTION:
        Convert a EdgeContext attributes into a dictionary.
        # PARAMETERS:
        None
        # RETURNS:
            dict
        Raises:
        """
        return {
            "id": self.id,
            "name": self.name,
            "board": self._board,
            "coord": self._coord,
            "occupant": self._occupant,
            "state": self._state,
        }