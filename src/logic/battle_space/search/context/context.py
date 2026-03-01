# src/logic/battle_space/searcher/map.py

"""
Module: logic.battle_space.searcher.map
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""

from typing import Optional

from logic.coord import Coord
from logic.system import SearchContext


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