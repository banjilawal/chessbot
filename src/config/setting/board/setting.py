# src/config/setting/board/dimension/setting.py

"""
Module: config.setting.board.dimension.setting
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Mapping, Optional
from types import MappingProxyType
from dataclasses import field

from config import BoardPropertyName, BoardPropertyValue

class BoardSetting:
    """
    Role
        - Property Settings
  
    Responsibilities:
        1.  Default Board properties.
  
    Attributes:
        value: BoardPropertyValue
  
    Provides:
  
    Super Class:
    """
    # _value: BoardPropertyValue = BoardPropertyValue()
    _entry: Dict[BoardPropertyName, int] = {
        BoardPropertyName.CELL_COUNT: BoardPropertyValue.board_size(),
        BoardPropertyName.NUMBER_OF_ROWS: BoardPropertyValue.num_rows(),
        BoardPropertyName.NUMBER_OF_COLUMNS: BoardPropertyValue.num_columns(),
        BoardPropertyName.MAX_ROW_INDEX: BoardPropertyValue.max_row_index(),
        BoardPropertyName.MAX_COLUMN_INDEX: BoardPropertyValue.max_column_index(),
        BoardPropertyName.DIAGONAL_LENGTH: BoardPropertyValue.diagonal_length(),
        BoardPropertyName.TEAM_SIZE: BoardPropertyValue.team_size(),
    }
    
    @classmethod
    def cell_count(cls) -> int:
        return cls._entry[BoardPropertyName.CELL_COUNT]
    
    @classmethod
    def numer_of_rows(cls) -> int:
        return cls._entry[BoardPropertyName.NUMBER_OF_ROWS]
    
    @classmethod
    def number_of_columns(cls) -> int:
        return cls._entry[BoardPropertyName.NUMBER_OF_COLUMNS]
    
    @classmethod
    def max_row_index(cls) -> int:
        return cls._entry[BoardPropertyName.MAX_ROW_INDEX]
    
    @classmethod
    def max_column_index(cls) -> int:
        return cls._entry[BoardPropertyName.MAX_COLUMN_INDEX]
    
    @classmethod
    def diagonal_length(cls) -> int:
        return cls._entry[BoardPropertyName.DIAGONAL_LENGTH]
    
    @classmethod
    def team_size(cls) -> int:
        return cls._entry[BoardPropertyName.TEAM_SIZE]