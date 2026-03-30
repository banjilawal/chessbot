# src/logic/coord/query/context/model/model.py

"""
Module: logic.coord.query.context.model.model
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Any, Dict, Optional

from logic.coord import Coord
from logic.system import Context


class CoordContext(Context[Coord]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Square attribute-value pair for a worker's execution path routing.

    Attributes:
        row: Optional[int]
        column: Optional[str]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    _row: Optional[int] = None
    _column: Optional[int] = None
    
    def __init__(self, row: Optional[int] = None, column: Optional[int] = None,):
        """
        Args:
            row: Optional[int]
            column: Optional[int]
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
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "row": self._row,
            "column": self._column,
        }
