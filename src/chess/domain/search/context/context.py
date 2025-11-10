# src/chess/domain/search/context/base.py

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
    _visitor_id: Optional[int] = None
    _visitor_name: Optional[str] = None
    _visitor_ransom: Optional[int] = None
    _visitor_coord: Optional[Coord] = None
    _visitor_rank: Optional[str] = None
    _visitor_team: Optional[str] = None
    _visitor_team_id: Optional[id] = None


    def __init__(
            self,
            visitor_id: Optional[int] = None,
            visitor_name: Optional[str] = None,
            visitor_ransom: Optional[int] = None,
            visitor_coord: Optional[Coord] = None,
            visitor_rank: Optional[str] = None,
            visitor_team: Optional[str] = None,
            visitor_team_id: Optional[id] = None
    ):
        self._visitor_id = visitor_id
        self._visitor_name = visitor_name
        self._visitor_coord = visitor_coord
        
        self._visitor_rank = visitor_rank
        self._visitor_ransom = visitor_ransom

        self._visitor_team = visitor_team
        self._visitor_team_id = visitor_team_id

        
    @property
    def visitor_id(self) -> Optional[int]:
        return self._visitor_id
    
    @property
    def visitor_name(self) -> Optional[str]:
        return self._visitor_name
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._visitor_coord
    
    @property
    def visitor_ransom(self) -> Optional[int]:
        return self._visitor_ransom
    
    @property
    def visitor_coord(self) -> Optional[Coord]:
        return self._visitor_coord

    @property
    def visitor_rank(self) -> Optional[str]:
        return self._visitor_rank
    
    @property
    def visitor_team_id(self) -> Optional[int]:
        return self.visitor_team_id
    
    @property
    def visitor_team(self) -> Optional[str]:
        return self._visitor_team
    
    @property
    def domain_id(self) -> Optional[int]:
        return self._domain_id
    
    def to_dict(self):
        return {
            "visitor_id": self._visitor_id,
            "visitor_name": self._visitor_name,
            "visitor_ransom": self._visitor_ransom,
            "visitor_coord": self._visitor_coord,
            "visitor_rank": self._visitor_rank,
            "visitor_team_id": self.visitor_team_id,
            "visitor_name": self._visitor_team
        }
