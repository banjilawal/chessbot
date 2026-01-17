# src/chess/token/factory/param/param.py

"""
Module: chess.token.factory.param.param
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from chess.coord import Coord
from chess.rank import Rank
from chess.square import Square
from chess.team import Team




class TokenBuildManifest:
    _id: int
    _rank: Rank
    _owner: Team
    coord: Coord
    _designation: str
    _roster_number: int
    _opening_square: Square
    
    def __init__(
            self,
            id: int,
            rank: Rank,
            owner: Team,
            coord: Coord,
            designation: str,
            roster_number: int,
            opening_square: Square,
    ):
        self._id = id
        self._rank = rank
        self._owner = owner
        self._coord = coord
        self._designation = designation
        self._roster_number = roster_number
        self._opening_square = opening_square
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def owner(self) -> Team:
        return self._owner
    
    @property
    def coord(self) -> Coord:
        return self._coord
    
    @property
    def designation(self) -> str:
        return self._designation
    
    @property
    def roster_number(self) -> int:
        return self._roster_number
    
    @property
    def opening_square(self) -> Square:
        return self._opening_square