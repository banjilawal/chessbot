# src/chess/target/target.py

"""
Module: chess.target.target
Author: Banji Lawal
Created: 2025-07-26
version: 1.0.0
"""


class Coord:
    """
    # ROLE: Data Object.
  
    # RESPONSIBILITY:
    1.  Row-column for locating Pieces and Squares on a chess board.
    2.  Primitive data type which binds items of different class hierarchies to the same location.
  
    # PROVIDES:
    Coord
  
    # ATTRIBUTES:
        *   row (int): Y-plane of the Board.
        *   column (int):  X-plane of the Board.
    """
    _row: int
    _column: int
    
    def __init__(self, row: int, column: int):
        """
        # ACTION:
        Construct a Coord instance.
        
        # PARAMETERS:
            *   row (int): index of row.
            *   column (int): index of column.
        
        # Returns:
        None
        
        # RAISES:
        None
        """
        method = "Coord.__init__"
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
        return f"Coord(row:{self._row} column:{self._column})"
