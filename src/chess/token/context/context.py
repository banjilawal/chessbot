# src/chess/piece/map.py

"""
Module: chess.piece.map
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional

from chess.team import Team
from chess.rank import Rank
from chess.piece import Piece
from chess.coord import Coord
from chess.system import Context, LoggingLevelRouter


class PieceContext(Context[Piece]):
    """
    # ROLE: Finder option filter

    # RESPONSIBILITIES:
    Provides options for what type of key-value pair PieceFinder should use to find matches.

    # PROVIDES:
    PieceContext.

    # ATTRIBUTES:
        *   team (Team)
        *   rank (Rank)
        *   ransom (str)
        *   coord (Coord)
    """
    _rank: Optional[Rank]
    _team: Optional[Team]
    _ransom: Optional[int]
    _coord: Optional[Coord]
    
    @LoggingLevelRouter.monitor
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            team: Optional[Team] = None,
            rank: Optional[Rank] = None,
            ransom: Optional[int] = None,
            coord: Optional[Coord] = None,
    ):
        super().__init__(id=id, name=name)
        self._coord = coord
        self._rank = rank
        self._team = team
        self._ransom = ransom

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
    
    def to_dict(self) -> {}:
        return {
            "id": self.id,
            "designation": self.name,
            "team": self._team,
            "rank": self._rank,
            "ransom": self._ransom,
            "coord": self._coord,
        }