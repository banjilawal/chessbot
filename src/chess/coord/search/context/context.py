# src/chess/coord/search/context/context.py

"""
Module: chess.coord.search.context.context
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.system import SearchContext


class CoordSearchContext(SearchContext):
    _row: Optional[int]
    _column: Optional[int]
    _coord: Optional[Coord]
    
    
    def __init__(self, row: Optional[int] = None, column: Optional[int] = None, coord: Optional[Coord] = None):
        self._row = row
        self._column = column
        self._coord = coord
        
        
    @property
    def row(self) -> Optional[int]:
        return self._row
    
    @property
    def column(self) -> Optional[int]:
        return self._column
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    def to_dict(self) -> {}:
        return {
            "row": self._row,
            "column": self._column,
            "coord": self._coord,
        }