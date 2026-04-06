# src/model/context/board/model.py

"""
Module: model.context.board.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class BoardContext(Context[Board]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Board attribute-value tuple which selects an execution path.

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
    _arena: Optional[Arena] = None
    
    def __init__( self, id: Optional[int] = None, arena: Optional[Arena] = None,):
        super().__init__(id=id, name=None)
        self._arena = arena
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def arena(self) -> Optional[Arena]:
        return self._arena
    
    def to_dict(self) -> dict:
        """
        # ACTION:
            Convert a SquareContext attributes into a dictionary.
        # PARAMETERS:
        None
        # RETURNS:
            dict
        Raises:
        """
        return {
            "id": self.id,
            "arena": self._arena
        }
