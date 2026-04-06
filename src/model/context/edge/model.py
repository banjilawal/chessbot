# src/model/context/edge/model.py

"""
Module: model.context.edge.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class EdgeContext(Context[Edge]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Square attribute-value tuple which selects an execution path.

    Attributes:
        id: Optional[int]
        team: Optional[Team]
        rank: Optional[Rank]
        ransom: Optional[int]
        current_position:Optional[Coord]
        designation: Optional[str]
        color: Optional[GameColor]
        opening_square_name: Optional[str]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
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
            "schema": self.designation,
            "board": self._board,
            "coord": self._coord,
            "occupant": self._occupant,
            "state": self._state,
        }