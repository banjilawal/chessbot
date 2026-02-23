# src/chess/square/map.py

"""
Module: chess.square.map
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from chess.board import Board
from chess.coord import Coord
from chess.square import Square


from chess.square.state import SquareState
from chess.system import Context
from chess.token import Token


class SquareContext(Context[Square]):
    """
    # ROLE: Factory, Switch, Attribute Selection

    # RESPONSIBILITIES:
    Factory that produces Context instances for searching Square datasets by different Square attributes.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   board (Optional[Board])
        *   coord (Optional[Coord])
        *   state (Optional[SquareState])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        Local:
            *   board (Optional[Board])
            *   coord (Optional[Coord])
            *   state (Optional[SquareState])

        Inherited:
            *   See Context class for inherited constructor parameters.

    # LOCAL METHODS:
        *   to_dict() -> dict

    # INHERITED METHODS:
        *   See StackService class for inherited methods.
    """
    _board: Optional[Board]
    _coord: Optional[Coord]
    _occupant: Optional[Token]
    _state: Optional[SquareState]
    
    def __init__(
            self,
            id: Optional[int],
            name: Optional[str],
            board: Optional[Board] = None,
            coord: Optional[Coord] = None,
            occupant: Optional[Token] = None,
            state: Optional[SquareState] = None,
    ):
        method = "SquareContext.__init__"
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