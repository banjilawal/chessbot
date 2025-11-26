# src/chess/checkmate/check.py

"""
Module: chess.checkmate.check.check
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""

from chess.coord import Coord


class KingLocationRecord:
    _id: int
    _king_id: int
    _king_name: str
    _team_id: int
    _team_name: str
    _king_position: Coord
    
    def __init__(self,
            id: int,
            king_id: int,
            king_name: str,
            team_id: int,
            team_name: str,
            king_position: Coord
    ):
        self._id = id
        self._king_id = king_id
        self._king_name = king_name
        self._team_id = team_id
        self._team_name = team_name
        self._king_position = king_position
        
    @property
    def id(self) -> int:
        return self._id
        
    @property
    def king_id(self) -> int:
        return self._king_id
    
    @property
    def king_name(self) -> str:
        return self._king_name
    
    @property
    def team_id(self) -> int:
        return self._team_id
    
    @property
    def team_name(self) -> str:
        return self._team_name
    
    @property
    def king_position(self) -> Coord:
        return self._king_position
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, KingLocationRecord):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return (
            f"king_id:{self._king_id}, "
            f"king_name:{self._king_name}, "
            f"team_id:{self._team_id}, "
            f"team_nam:{self._team_name}, "
            f"king_position:{self._king_position}"
        )
    
    def __repr__(self):
        return (f"<KingLocationRecord king_id={self._king_id} king_name={self._king_name} "
                f"team_id={self._team_id} team_name={self._team_name} "
                f"king_position={self._king_position}>")