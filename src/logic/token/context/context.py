# src/logic/token/map.py

"""
Module: logic.token.map
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional

from logic.square import Square
from logic.team import Team
from logic.rank import Rank
from logic.token import Token
from logic.coord import Coord
from logic.system import Context, GameColor, LoggingLevelRouter


class TokenContext(Context[Token]):
    """
    # ROLE: SearchWorker option filter

    # RESPONSIBILITIES:
    Provides options for what type of key-value pair TokenFinder should use to find matches.

    # PROVIDES:
    TokenContext.

    # ATTRIBUTES:
        *   team (Team)
        *   rank (Rank)
        *   ransom (str)
        *   coord (Coord)
        *   opening_square_name_name (Square)
    """
    _rank: Optional[Rank]
    _team: Optional[Team]
    _ransom: Optional[int]
    _coord: Optional[Coord]
    _color: Optional[GameColor]
    _designation: Optional[str]
    _opening_square_name: Optional[Square]
    
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
            opening_square_name: Optional[str] = None
    ):
        super().__init__(id=id, name=None)
        self._coord = coord
        self._rank = rank
        self._team = team
        self._ransom = ransom
        self._color = color
        self._designation = designation
        self._opening_square_name = opening_square_name

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
    def opening_square_name(self) -> Optional[str]:
        return self._opening_square_name
    
    def to_dict(self) -> {}:
        return {
            "id": self.id,
            "team": self._team,
            "rank": self._rank,
            "color": self._color,
            "coord": self._coord,
            "ransom": self._ransom,
            "designation": self.designation,
            "opening_square_name_name": self._opening_square_name
        }