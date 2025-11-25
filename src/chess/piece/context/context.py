# src/chess/piece/context/context.py

"""
Module: chess.piece.context.context
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Dict, Optional

from chess.piece import Piece
from chess.coord import Coord
from chess.rank import Rank
from chess.system import Context, LoggingLevelRouter
from chess.team import Team


class PieceContext(Context[Piece]):
    """
    # ROLE: Search option filter

    # RESPONSIBILITIES:
    Provides options for what type of key-value pair PieceSearch should use to find matches.

    # PROVIDES:
    PieceContext.

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   coord (Coord)
    """
    _coord: Optional[Coord]
    _rank: Optional[Rank]
    _tean: Optional[Team]
    _ransom: Optional[int]
    
    @LoggingLevelRouter.monitor
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            coord: Optional[Coord] = None,
            rank: Optional[Rank] = None,
            team: Optional[Team] = None,
            ransom: Optional[int] = None,
    ):
        super().__init__(id=id, name=name)
        self._coord = coord
        self._rank = rank
        self._team = team
        self._ransom = ransom
        
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    @property
    def name(self) -> Optional[str]:
        return self._visitor_name
    
    @property
    def rank(self) -> Optional[Rank]:
        return self._rank_name
    
    @property
    def ransom(self) -> Optional[int]:
        return self._ransom
    
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "team": self._team,
            "rank": self._rank,
            "ransom": self._ransom,
        }