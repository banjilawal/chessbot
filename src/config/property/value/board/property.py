# src/config/property/value/board/property.py

"""
Module: config.property.value.board.property
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from math import sqrt


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
    _DIMENSION = 8
    _num_rows: int = _DIMENSION
    _num_columns: int = _DIMENSION
        
    @classmethod
    def board_size(cls) -> int:
        return cls._num_rows * cls._num_columns
    
    @classmethod
    def num_rows(cls) -> int:
        return cls._num_rows
    
    @classmethod
    def num_columns(cls) -> int:
        return cls._num_columns
    
    @classmethod
    def max_row_index(cls) -> int:
        return cls._num_rows - 1
    
    @classmethod
    def max_column_index(cls) -> int:
        return cls._num_columns - 1
    
    @classmethod
    def diagonal_length(cls) -> int:
        return sqrt(cls._num_rows**2 + cls._num_columns**2)
    
        
        