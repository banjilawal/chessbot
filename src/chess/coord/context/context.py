# src/chess/coord/context/context

"""
Module: chess.coord.context.context
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.system import Context


class CoordContext(Context[Coord]):
    """
    # ROLE: Search option filter
  
    # RESPONSIBILITIES:
    Provides options for what type of key-value pair CoordSearch should use to find matches.
  
    # PROVIDES:
    CoordContext.
  
    # ATTRIBUTES:
        *   row (int)
        *   column (int)
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
        method = "CoordContext.to_dict"
        return {
            "row": self._row,
            "column": self._column,
        }
