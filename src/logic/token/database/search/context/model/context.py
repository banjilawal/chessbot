# src/logic/token/database/search/context/model/context.py

"""
Module: logic.token.database.search.context.model.context
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from logic.team import Team
from logic.rank import Rank
from logic.token import Token
from logic.coord import Coord
from logic.system import Context, GameColor, LoggingLevelRouter


class TokenContext(Context[Token]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Token attribute-value pair for a worker's execution path routing.

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
    _rank: Optional[Rank]
    _team: Optional[Team]
    _ransom: Optional[int]
    _color: Optional[GameColor]
    _designation: Optional[str]
    _current_position:Optional[Coord]
    _opening_square_name: Optional[str]
    
    @LoggingLevelRouter.monitor
    def __init__(
            self,
            id: Optional[int] = None,
            team: Optional[Team] = None,
            rank: Optional[Rank] = None,
            ransom: Optional[int] = None,
            designation: Optional[str] = None,
            color: Optional[GameColor] = None,
            current_position: Optional[Coord] = None,
            opening_square_name: Optional[str] = None
    ):
        """
        Args:
            id: Optional[int]
            team: Optional[Team]
            rank: Optional[Rank]
            ransom: Optional[int]
            current_position:Optional[Coord]
            designation: Optional[str]
            color: Optional[GameColor]
            opening_square_name: Optional[str]
        """
        super().__init__(id=id, name=None)
        self._rank = rank
        self._team = team
        self._color = color
        self._ransom = ransom
        self._designation = designation
        self._current_position = current_position
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
    def color(self) -> Optional[GameColor]:
        return self._color
    
    @property
    def designation(self) -> Optional[str]:
        return self._designation
    
    @property
    def current_position(self) -> Optional[Coord]:
        return self._current_position
    
    @property
    def opening_square_name(self) -> Optional[str]:
        return self._opening_square_name
    
    def to_dict(self) -> {}:
        return {
            "id": self.id,
            "team": self._team,
            "rank": self._rank,
            "color": self._color,
            "ransom": self._ransom,
            "designation": self.designation,
            "current_position": self._current_position,
            "opening_square_name_name": self._opening_square_name
        }