# src/chess/square/search/context/context

"""
Module: chess.square.search.context.context
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.system import SearchContext


class CoordSearchContext(SearchContext):
    """
    # ROLE: Search option filter
  
    # RESPONSIBILITIES:
    Provides options for what type of key-value pair CoordSearch implementations use to find matches.
  
    # PROVIDES:
    CoordSearchContext.
  
    # ATTRIBUTES:
        *   row (int): Find items whose row matches this value.
        *   column (str): Find items whose column matches this value.
        *   square (Coord): Find items whose square matches this value.
    """
    
    _row: Optional[int] = None
    _column: Optional[str] = None
    _coord: Optional[Coord] = None
    
    def __init__(
            self,
            row: Optional[int] = None,
            column: Optional[str] = None,
            coord: Optional[Coord] = None,
    ):
        self._row = row
        self._column = column
        self._coord = coord
    
    
    @property
    def row(self) -> Optional[int]:
        return self._row
    
    
    @property
    def column(self) -> Optional[str]:
        return self._column
    
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    
    def to_dict(self) -> dict:
        return {
            "row": self._row,
            "column": self._column,
            "square": self._coord
        }
