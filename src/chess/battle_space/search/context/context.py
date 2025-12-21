# src/chess/battle_space/searcher/map/map.py

"""
Module: chess.battle_space.searcher.map.map
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.system import SearchContext


class ProjectionSearchContext(SearchContext):
    """"""
    
    @property
    def id(self) -> Optional[int]:
        return self._piece_id
    
    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._position
    
    @property
    def ransom(self) -> Optional[int]:
        return self._ransom
    
    def to_dict(self) -> dict:
        return {
            "visitor_id": self._piece_id,
            "visitor_name": self._name,
            "point": self._position
        }