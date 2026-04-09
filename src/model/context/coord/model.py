# src/model/context/coord/model.py

"""
Module: model.context.coord.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class CoordContext(Context[Coord]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Coord attribute-value search filter.

    Attributes:
            row: Optional[int]
            column: Optional[int]

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
