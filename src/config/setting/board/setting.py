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
                BoardPropertyName.DIMENSION: BoardPropertyValue.board_size(),
                BoardPropertyName.NUMBER_OF_ROWS: BoardPropertyValue.num_rows(),
                BoardPropertyName.NUMBER_OF_COLUMNS: BoardPropertyValue.num_columns(),
                BoardPropertyName.MAX_ROW_INDEX: BoardPropertyValue.max_row_index(),
                BoardPropertyName.MAX_COLUMN_INDEX: BoardPropertyValue.max_column_index(),
            }
    
    # def __init__(
    #         cls,
    #         value: Optional[BoardPropertyValue] | None = None,
    # ):
    #     """
    #     Args:
    #         value: Optional[BoardPropertyValue]
    #     """
    # 
    #     _vale = value or BoardPropertyValue()
    #     _entry = Mapping[BoardPropertyName, int] = field(
    #         default_factory=lambda: MappingProxyType(
    #             {
    #                 BoardPropertyName.DIMENSION: _value.board_size,
    #                 BoardPropertyName.NUMBER_OF_ROWS: _value.number_of_rows,
    #                 BoardPropertyName.NUMBER_OF_COLUMNS: _value.number_of_columns,
    #                 BoardPropertyName.MAX_ROW_INDEX: _value.number_of_rows - 1,
    #                 BoardPropertyName.MAX_COLUMN_INDEX: _value.number_of_columns - 1,
    #                 BoardPropertyName.KNIGHT_RADIUS: _value.number_of_columns,
    #             }
    #         )
    #     )
        
    # @classmethod
    # def entry(cls) -> Mapping[BoardPropertyName, int]:
    #     return _entry
    
    @classmethod
    def dimension(cls) -> int:
        return cls._entry[BoardPropertyName.DIMENSION]
    
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