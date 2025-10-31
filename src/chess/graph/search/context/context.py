# src/chess/graph/search/context/context.py

"""
Module: chess.graph.search.context.context
Author: Banji Lawal
Created: 2025-10-31
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.system import SearchContext


class GraphSearchContext(SearchContext):
    """"""
    pass
    _ransom: Optional[int] = None
    _rank_name: Optional[str] = None
    _piece_id: Optional[int] = None
    _piece_name: Optional[str] = None
    _piece_address: Optional[Coord]
    _team_id: Optional[id] = None
    _team_name: Optional[str] = None
    _domain_id: Optional[int] = None
    _point: Optional[Coord] = None
    
    def __init__(
            self,
            ransom: Optional[int] = None,
            rank_name: Optional[str] = None,
            piece_id: Optional[int] = None,
            piece_name: Optional[str] = None,
            piece_address: Optional[Coord] = None,
            team_id: Optional[id] = None,
            team_name: Optional[str] = None,
            domain_id: Optional[int] = None,
            point: Optional[Coord] = None,
    ):
        self._ransom = ransom
        self._rank_name = rank_name
        self._piece_id = piece_id
        self._piece_name = piece_name
        self._piece_address = piece_address
        self._team_id = team_id
        self._team_name = team_name
        self._domain_id = domain_id
        self._point = point
    
    @property
    def ransom(self) -> Optional[int]:
        return self._ransom
    
    @property
    def rank_name(self) -> Optional[str]:
        return self._rank_name
    
    @property
    def piece_id(self) -> Optional[int]:
        return self._piece_id
    
    def piece_name(self) -> Optional[str]:
        return self._piece_name
    
    def piece_address(self) -> Optional[Coord]:
        return self._piece_address
    
    @property
    def team_id(self) -> Optional[int]:
        return self._team_id
    
    @property
    def team_name(self) -> Optional[str]:
        return self._team_name
    
    @property
    def domain_id(self) -> Optional[int]:
        return self._domain_id
    
    @property
    def point(self) -> Optional[Coord]:
        return self._point
    
    def to_dict(self):
        return {
            "ransom": self._ransom,
            "rank_name": self._rank_name,
            "piece_id": self._piece_id,
            "piece_name": self._piece_name,
            "team_id": self._team_id,
            "team_name": self._team_name,
            "domain_id": self._domain_id,
            "point": self._point
        }
