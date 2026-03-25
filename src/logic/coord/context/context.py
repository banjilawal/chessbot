# src/logic/coord/query/query.py

"""
Module: logic.coord.query.query
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional

from logic.coord import Coord
from logic.system import Context


class CoordContext(Context[Coord]):
    """
    Role:Filter, Search, Selection, Reverse/Forward Lookups

    Responsibilities:
    Provide an CoordFinder with an attribute-value which finds Coords which match the targeted attribute-value.

    Super Class:
        *   Context

    Provides:

    # LOCAL ATTRIBUTES:
        *   row (Optional[int])
        *   coord (Optional[Coord])
        *   column (Optional[int])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _row: Optional[int] = None
    _column: Optional[int] = None
    
    def __init__(self, row: Optional[int] = None, column: Optional[int] = None,):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   row (Optional[int])
            *   coord (Optional[Coord])
            *   column (Optional[int])
        # RETURNS:
            None
        Raises:
            None
        """
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
