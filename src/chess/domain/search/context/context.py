# src/chess/domain/searcher/context/exception.py

"""
Module: chess.domain.searcher.context.context
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.system import SearchContext


class ResidentFilter(SearchContext):
    """"""
    _id: Optional[int] = None
    _name: Optional[str] = None
    _ransom: Optional[int] = None
    _coord: Optional[Coord] = None
    _rank_name: Optional[str] = None
    _team_name: Optional[str] = None
    _team_id: Optional[id] = None


    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            ransom: Optional[int] = None,
            coord: Optional[Coord] = None,
            rank: Optional[str] = None,
            team: Optional[str] = None,
            team_id: Optional[id] = None
    ):
        self._id = id
        self._name = name
        self._coord = coord
        self._rank_name = rank
        self._ransom = ransom
        self._team_name = team
        self._team_id = team_id

        
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    @property
    def ransom(self) -> Optional[int]:
        return self._ransom
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord

    @property
    def rank(self) -> Optional[str]:
        return self._rank_name
    
    @property
    def team_id(self) -> Optional[int]:
        return self.team_id
    
    @property
    def team(self) -> Optional[str]:
        return self._team_name
    
    def to_dict(self):
        return {
            "id": self._id,
            "designation": self._name,
            "ransom": self._ransom,
            "target": self._coord,
            "rank_name": self._rank_name,
            "team_id": self.team_id,
            "team_name": self._team_name
        }
