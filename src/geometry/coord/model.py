# src/geometry/coord/model.py
"""
Module: geometry.coord.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

class Coord:
    """
    Role:
        -   Addressing
        -   Data-Holder
  
    Responsibilities:
        1.  Provide global, low-level addressing squares and tokens on the board.
        
    Attributes:
        row: int
        column: int
        
    Provides:
    
    Super Class:
    """
    _row: int
    _column: int
    
    def __init__(self, row: int, column: int):
        """
        Args:
            row: int
            column: int
        """
        self._row = row
        self._column = column
    
    @property
    def row(self) -> int:
        return self._row
    
    @property
    def column(self) -> int:
        return self._column
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Coord):
            return self._row == other.row and self._column == other.column
        return False
    
    def __hash__(self):
        return hash((self._row, self._column))
    
    def __str__(self):
        return f"Coord{{(row:{self._row}, column:{self._column}}})"
