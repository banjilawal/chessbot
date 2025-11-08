# src/chess/domain/search/context/context.py

"""
Module: chess.domain.search.context.context
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.system import SearchContext


class VisitorSearchContext(SearchContext):
    """"""
    _id: Optional[int] = None
    _name: Optional[str] = None
    _ransom: Optional[int] = None
    _coord: Optional[Coord] = None
    _rank_name: Optional[str] = None
    _team_id: Optional[id] = None
    _team_name: Optional[str] = None

    def __init__(
            self,
            _id: Optional[int] = None,
            _name: Optional[str] = None,
            _ransom: Optional[int] = None,
            _coord: Optional[Coord] = None,
            _rank_name: Optional[str] = None,
            _team_id: Optional[id] = None,
            _team_name: Optional[str] = None
    ):
        self._id = _id
        self._name = _name
        self._coord = _coord
        self._ransom = _ransom
        self._rank_name = _rank_name
        self._team_id = _team_id
        self._team_name = _team_name
        
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
    def rank_name(self) -> Optional[str]:
        return self._visitor_rank
    
    @property
    def team_id(self) -> Optional[int]:
        return self._team_id
    
    @property
    def team_name(self) -> Optional[str]:
        return self._team_name
    
    @property
    def domain_id(self) -> Optional[int]:
        return self._domain_id
    
    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "ransom": self._ransom,
            "coord": self._coord,
            "rank_name": self._rank_name,
            "team_id": self._team_id,
            "team_name": self._team_name
        }
