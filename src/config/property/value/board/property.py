# src/config/property/value/board/property.py

"""
Module: config.property.value.board.property
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional


class BoardPropertyValue:
    """
     Role:
        1.  Configuration
        2.  Metadata

     Responsibilities:
         1. Values of BoardProperty attribute.

     Attributes:
        board_size: int
        number_of_rows: int
        number_of_columns: int
        
        max_row_index: int
        max_column_index: int
        
     Provides:

     Super Class:
     """
    DIMENSION = 8
    _board_size: int
    _number_of_rows: int
    _number_of_columns: int
    
    def __init__(
            self,
            board_size: Optional[int] | None = None,
            number_of_rows: Optional[int] | None = None,
            number_of_columns: Optional[int] | None = None,
    ):
        """
        Args:
            board_size: Optional[int]
            number_of_rows: Optional[int]
            number_of_columns: Optional[int]
        """
        self._board_size = board_size or self.DIMENSION
        self._number_of_rows = number_of_rows or self.DIMENSION
        self._number_of_columns = number_of_columns or self.DIMENSION
        
    @property
    def board_size(self) -> int:
        return self._board_size
    
    @property
    def number_of_rows(self) -> int:
        return self._number_of_rows
    
    @property
    def number_of_columns(self) -> int:
        return self._number_of_columns
    
    @property
    def max_row_index(self) -> int:
        return self._number_of_rows - 1
    
    @property
    def max_column_index(self) -> int:
        return self._number_of_columns - 1
    
        
        