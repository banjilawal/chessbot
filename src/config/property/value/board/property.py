# src/config/property/value/board/property.py

"""
Module: config.property.value.board.property
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations



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
    _number_of_rows: int = _DIMENSION
    _number_of_columns: int = _DIMENSION
    
    # def __init__(
    #         cls,
    #         board_size: Optional[int] | None = None,
    #         number_of_rows: Optional[int] | None = None,
    #         number_of_columns: Optional[int] | None = None,
    # ):
    #     """
    #     Args:
    #         board_size: Optional[int]
    #         number_of_rows: Optional[int]
    #         number_of_columns: Optional[int]
    #     """
    #     cls._board_size = board_size or cls._DIMENSION
    #     cls._number_of_rows = number_of_rows or cls._DIMENSION
    #     cls._number_of_columns = number_of_columns or cls._DIMENSION
        
    @classmethod
    def board_size(cls) -> int:
        return cls._number_of_rows * cls._number_of_columns
    
    @classmethod
    def num_rows(cls) -> int:
        return cls._number_of_rows
    
    @classmethod
    def num_columns(cls) -> int:
        return cls._number_of_columns
    
    @classmethod
    def max_row_index(cls) -> int:
        return cls._number_of_rows - 1
    
    @classmethod
    def max_column_index(cls) -> int:
        return cls._number_of_columns - 1
    
        
        