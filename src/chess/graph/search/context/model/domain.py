# src/chess/points/searcher/exception.py

"""
Module: chess.points.searcher.map
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""


from typing import Optional

from chess.piece import Piece
from chess.coord import Coord
from chess.graph import GraphSearchContext



class GraphDomainFilter(GraphSearchContext):
    """"""
    _id: Optional[int] = None
    _name: Optional[str] = None
    _root: Optional[Coord] = None
    _previous_root: Optional[Coord] = None
    _ransom: Optional[int] = None
    _rank_name: Optional[str] = None
    _team_id: Optional[id] = None
    _team_name: Optional[str] = None
    _point: Optional[Coord] = None
    _resident: Optional[Piece] = None
    
    
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            ransom: Optional[int] = None,
            root: Optional[Coord] = None,
            rank_name: Optional[str] = None,
            team_id: Optional[id] = None,
            team_name: Optional[str] = None,
            previous_root: Optional[Coord] = None,
            point: Optional[Coord] = None,
            resident: Optional[Piece] = None,
    ):
        self._id = id
        self._name = name
        self._root = root
        self._ransom = ransom
        self._rank_name = rank_name
        self._team_id = team_id
        self._team_name = team_name
        self._previous_root = previous_root
        self._point = point
        self._resident = resident
  
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    
    @property
    def name(self) -> Optional[str]:
        return self._name
    
    
    @property
    def root(self) -> Optional[Coord]:
        return self._root
    
    
    @property
    def ransom(self) -> Optional[int]:
        return self._ransom
   
    
    @property
    def previous_root(self) -> Optional[Coord]:
        return self._previous_root
    
    
    @property
    def rank_name(self) -> Optional[str]:
        return self._rank_name
    
    
    @property
    def team_id(self) -> Optional[int]:
        return self._team_id
    
    
    @property
    def team_name(self) -> Optional[str]:
        return self._team_name
    
    
    @property
    def point(self) -> Optional[Coord]:
        return self._point
    
    @property
    def resident(self) -> Optional[Piece]:
        return self._resident
    
    
    def to_dict(self):
        return {
            "id": self._id,
            "designation": self._name,
            "ransom": self._ransom,
            "rank_name": self._rank_name,
            "team_name": self._team_name,
            "team_id": self._team_id,
            "root": self._root,
            "previous_root": self._previous_root,
            "point": self._point,
        }
