# src/chess/token/map.py

"""
Module: chess.token.map
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional

from chess.square import Square
from chess.team import Team
from chess.rank import Rank
from chess.token import Token
from chess.coord import Coord
from chess.system import Context, GameColor, LoggingLevelRouter


class TokenContext(Context[Token]):
    """
    # ROLE: AbstractSearcher option filter

    # RESPONSIBILITIES:
    Provides options for what type of key-value pair TokenFinder should use to find matches.

    # PROVIDES:
    TokenContext.

    # ATTRIBUTES:
        *   team (Team)
        *   rank (Rank)
        *   ransom (str)
        *   coord (Coord)
        *   opening_square_name (Square)
    """
    _rank: Optional[Rank]
    _team: Optional[Team]
    _ransom: Optional[int]
    _coord: Optional[Coord]
    _color: Optional[GameColor]
    _designation: Optional[str]
    _opening_square: Optional[Square]
    
    @LoggingLevelRouter.monitor
    def __init__(
            self,
            id: Optional[int] = None,
            team: Optional[Team] = None,
            rank: Optional[Rank] = None,
            ransom: Optional[int] = None,
            coord: Optional[Coord] = None,
            designation: Optional[str] = None,
            color: Optional[GameColor] = None,
            opening_square: Optional[Square] = None
    ):
        super().__init__(id=id, name=None)
        self._coord = coord
        self._rank = rank
        self._team = team
        self._ransom = ransom
        self._color = color
        self._designation = designation
        self._opening_square = opening_square

    @property
    def team(self) -> Optional[Team]:
        return self._team
   
    @property
    def rank(self) -> Optional[Rank]:
        return self._rank
    
    @property
    def ransom(self) -> Optional[int]:
        return self._ransom
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    @property
    def designation(self) -> Optional[str]:
        return self._designation
    
    @property
    def opening_square(self) -> Optional[Square]:
        return self._opening_square
    
    def to_dict(self) -> {}:
        return {
            "id": self.id,
            "team": self._team,
            "rank": self._rank,
            "color": self._color,
            "coord": self._coord,
            "ransom": self._ransom,
            "designation": self.designation,
            "opening_square_name": self._opening_square
        }