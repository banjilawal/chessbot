# src/config/setting/board/dimension/setting.py

"""
Module: config.setting.board.dimension.setting
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Mapping, Optional
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
    _value: BoardPropertyValue
    _entry: Mapping[BoardPropertyName, int]
    
    def __init__(
            self,
            value: Optional[BoardPropertyValue] | None = None,
    ):
        """
        Args:
            value: Optional[BoardPropertyValue]
        """

        self._vale = value or BoardPropertyValue()
        self._entry = Mapping[BoardPropertyName, int] = field(
            default_factory=lambda: MappingProxyType(
                {
                    BoardPropertyName.DIMENSION: self._value.board_size,
                    BoardPropertyName.NUMBER_OF_ROWS: self._value.number_of_rows,
                    BoardPropertyName.NUMBER_OF_COLUMNS: self._value.number_of_columns,
                    BoardPropertyName.MAX_ROW_INDEX: self._value.number_of_rows - 1,
                    BoardPropertyName.MAX_COLUMN_INDEX: self._value.number_of_columns - 1,
                    BoardPropertyName.KNIGHT_RADIUS: self._value.number_of_columns,
                }
            )
        )
        
    @property
    def entry(self) -> Mapping[BoardPropertyName, int]:
        return self._entry
    
    @property
    def dimension(self) -> int:
        return self._entry[BoardPropertyName.DIMENSION]
    
    @property
    def numer_of_rows(self) -> int:
        return self._entry[BoardPropertyName.NUMBER_OF_ROWS]
    
    @property
    def number_of_columns(self) -> int:
        return self._entry[BoardPropertyName.NUMBER_OF_COLUMNS]
    
    @property
    def max_row_index(self) -> int:
        return self._entry[BoardPropertyName.MAX_ROW_INDEX]
    
    @property
    def max_column_index(self) -> int:
        return self._entry[BoardPropertyName.MAX_COLUMN_INDEX]