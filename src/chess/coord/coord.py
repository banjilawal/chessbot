# src/chess/coord/coord.py

"""
Module: chess.coord.coord
Author: Banji Lawal
Created: 2025-07-26
version: 1.0.0
"""


class Coord:
    """
    # ROLE: Addressing, Data Object
  
    # RESPONSIBILITY:
    1.  Provide global, low-level addressing for referencing bag on Board by row and column indexes.
    
    # PARENT:
    None
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
        *   row (int)
        *   column (int)
    
    INHERITED ATTRIBUTES:
    None
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
        
        # RETURNS:
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
        return f"Coord{{(row:{self._row}, column:{self._column}}})"
