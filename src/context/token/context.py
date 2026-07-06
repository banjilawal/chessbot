# src/context/token/model/state.py

"""
Module: context.token.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional

from context import Context
from model import Coord, HomeSquare, Rank, Team, Token
from setting import GameColor


class TokenContext(Context[Token]):
        """
        Role:
            -   Selection
            -   Routing mask
            -   Data-Holder
    
        Responsibilities:
            1.  Supply a Token attribute-value search filter.
    
        Attributes:
            id: Optional[int]
            team: Optional[Team]
            rank: Optional[Rank]
            ransom: Optional[int]
            current_position:Optional[Coord]
            designation: Optional[str]
            color: Optional[GameColor]
            home_square: Optional[HomeSquare]
    
        Provides:
            -   to_dict() -> Dict[str, Any]
    
        Super Class:
            Context
        """
        _id: Optional[int] | None = None
        _rank: Optional[Rank] | None = None
        _team: Optional[Team] | None = None
        _ransom: Optional[int] | None = None
        _color: Optional[GameColor] | None = None
        _designation: Optional[str] | None = None
        _current_position:Optional[Coord] | None = None
        _home_square: Optional[HomeSquare] | None = None
        
        def __init__(
            self,
            id: Optional[int] | None = None,
            rank: Optional[Rank] | None = None,
            team: Optional[Team] | None = None,
            ransom: Optional[int] | None = None,
            color: Optional[GameColor] | None = None,
            designation: Optional[str] | None = None,
            current_position: Optional[Coord] | None = None,
            home_square: Optional[HomeSquare] | None = None,
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
                home_square: Optional[HomeSquare]
            """
            super().__init__(id=id, name=designation)
            self._rank = rank
            self._team = team
            self._ransom = ransom
            self._color = color
            self._designation = designation
            self._home_square = home_square
            self._current_position = current_position
            
        @property
        def rank(self) -> Optional[Rank]:
            return self._rank
        
        @property
        def team(self) -> Optional[Team]:
            return self._team
        
        @property
        def ransom(self) -> Optional[int]:
            return self._ransom
        
        @property
        def color(self) -> Optional[GameColor]:
            return self._color
        
        @property
        def home_square(self) -> Optional[HomeSquare]:
            return self._home_square
        
        @property
        def current_position(self) -> Optional[Coord]:
            return self._current_position
    
        @property
        def designation(self) -> Optional[str]:
            return self._designation
    
        @property
        def to_dict(self) -> Dict[str, Any]:
            return {
                "id": self.id,
                "team": self._team,
                "rank": self._rank,
                "color": self._color,
                "ransom": self._ransom,
                "designation": self._designation,
                "current_position": self._current_position,
                "home_square": self._home_square
            }