# src/chess/square/search/context/context

"""
Module: chess.square.search.context.context
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional


from chess.system import SearchContext
from chess.coord import Coord, CoordSearchContext, CoordValidator
from chess.system.context import ContextMaskList


class CoordSearchContext(SearchContext):
    """
    # ROLE: Search option filter
  
    # RESPONSIBILITIES:
    Provides options for what type of key-value pair CoordSearchService implementations use to find matches.
  
    # PROVIDES:
    CoordSearchContext.
  
    # ATTRIBUTES:
        *   row (int): Find items whose row matches this value.
        *   column (str): Find items whose column matches this value.
        *   square (Coord): Find items whose square matches this value.
    """
    
    _row: Optional[int] = None
    _column: Optional[int] = None
    
    def __init__(
            self,
            row: Optional[int] = None,
            column: Optional[int] = None,
    ):
        super().__init__(id=None, name=None)
        self._row = row
        self._column = column
    
    @property
    def row(self) -> Optional[int]:
        return self._row
    
    @property
    def column(self) -> Optional[int]:
            return self._column
    
    def to_dict(self) -> dict:
        return {
            "row": self._row,
            "column": self._column,
        }
