# src/chess/checkmate/check.py

"""
Module: chess.checkmate.check.check
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""

from chess.coord import Coord


class CheckRecord:
    _id: int
    _poster_id: int
    _poster_name: str
    _poster_position: Coord
    _king_id: int
    _king_name: str
    _king_position: Coord
    
    def __init__(self,
            id: int,
            poster_id: int,
            poster_name: str,
            poster_position: Coord,
            king_id: int,
            king_name: str,
            king_position: Coord
    ):
        self._id = id
        self._poster_id = poster_id
        self._poster_name = poster_name
        self._poster_position = poster_position
        self._king_id = king_id
        self._king_name = king_name
        self._king_position = king_position
        
    @property
    def id(self) -> int:
        return self._id
        
    @property
    def poster_id(self) -> int:
        return self._poster_id
    
    @property
    def poster_name(self) -> str:
        return self._poster_name
    
    @property
    def poster_position(self) -> Coord:
        return self._poster_position
    
    @property
    def king_id(self) -> int:
        return self._king_id
    
    @property
    def king_name(self) -> str:
        return self._king_name
    
    @property
    def king_position(self) -> Coord:
        return self._king_position
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, CheckRecord):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return (
            f"poster_id:{self._poster_id}, "
            f"poster_name:{self._poster_name}, "
            f"poster_position:{self._poster_position}, "
            f"king_id:{self._king_id}, "
            f"king_nam:{self._king_name}, "
            f"king_position:{self._king_position}"
        )
    
    def __repr__(self):
        return (f"<KingCheckRecord poster_id={self._poster_id} poster_name={self._poster_name} "
                f"poster_position={self._poster_position} king_id={self._king_id} king_name={self._king_name} "
                f"king_position={self._king_position}>")