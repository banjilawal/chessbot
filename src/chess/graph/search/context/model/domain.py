# src/chess/domain/search/context/base.py

"""
Module: chess.domain.search.context.context
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""


from typing import Optional

from chess.coord import Coord
from chess.graph import GraphSearchContext


class GraphDomainFilter(GraphSearchContext):
    """"""
    _domain_id: Optional[int] = None
    _domain_name: Optional[str] = None
    _domain_root: Optional[Coord] = None
    _domain_previous_root: Optional[Coord] = None
    _domain_ransom: Optional[int] = None
    _domain_rank: Optional[str] = None
    _domain_team_id: Optional[id] = None
    _domain_team: Optional[str] = None
    _visitor_coord: Optional[Coord] = None
    
    
    def __init__(
            self,
            domain_id: Optional[int] = None,
            domain_name: Optional[str] = None,
            domain_ransom: Optional[int] = None,
            domain_root: Optional[Coord] = None,
            domain_rank: Optional[str] = None,
            domain_team_id: Optional[id] = None,
            domain_team: Optional[str] = None,
            visitor_coord: Optional[Coord] = None,
            domain_previous_root: Optional[Coord] = None,
    ):
        self._domain_id = domain_id
        self._domain_name = domain_name
        self._domain_root = domain_root
        self._domain_ransom = domain_ransom
        self._domain_rank = domain_rank
        self._domain_team_id = domain_team_id
        self._domain_team = domain_team
        self._visitor_coord = visitor_coord
        self._domain_previous_root = domain_previous_root
  
    
    @property
    def domain_id(self) -> Optional[int]:
        return self._domain_id
    
    
    @property
    def domain_name(self) -> Optional[str]:
        return self._domain_name
    
    
    @property
    def domain_root(self) -> Optional[Coord]:
        return self._domain_root
    
    
    @property
    def domain_ransom(self) -> Optional[int]:
        return self._domain_ransom
   
    
    @property
    def domain_previous_root(self) -> Optional[Coord]:
        return self._domain_previous_root
    
    
    @property
    def domain_rank(self) -> Optional[str]:
        return self._domain_rank
    
    
    @property
    def domain_team_id(self) -> Optional[int]:
        return self._domain_team_id
    
    
    @property
    def domain_team(self) -> Optional[str]:
        return self._domain_team
    
    
    @property
    def visitor_coord(self) -> Optional[Coord]:
        return self._visitor_coord
    
    
    def to_dict(self):
        return {
            "domain_id": self._id,
            "domain_name": self._domain_name,
            "domain_ransom": self._domain_ransom,
            "domain_rank": self._domain_rank,
            "domain_team": self._domain_team,
            "domain_team_id": self._domain_team_id,
            "domain_root": self._domain_root,
            "domain_previous_root": self._domain_previous_root,
            "visitor_coord": self._visitor_coord,
        }
