# src/setting/board/dimension/setting.py

"""
Module: setting.board.dimension.setting
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field

__all__ = [
    "BoardDimensionProperty",
]

from setting import BoardProperty

__all__ = [
    # ======================# BOARD_DIMENSION_PROPERTY #======================#
    "BoardDimensionProperty",
]

board_size = 8
knight_radius = 2
number_of_rows = board_size
number_of_columns = board_size



@dataclass
class BoardDimensionProperty:
    """
    Role
        -   Property Settings
  
    Responsibilities:
        1.  Default Board properties.
  
    Attributes:
  
    Provides:
  
    Super Class:
        Enum
    """
    entry: Mapping[BoardProperty, int] = field(
        default_factory=lambda: MappingProxyType(
            {
                BoardProperty.DIMENSION: board_size,
                BoardProperty.NUMBER_OF_ROWS: number_of_rows,
                BoardProperty.NUMBER_OF_COLUMNS: number_of_columns,
                BoardProperty.MAX_ROW_INDEX: number_of_rows - 1,
                BoardProperty.MAX_COLUMN_INDEX: number_of_columns - 1,
                BoardProperty.KNIGHT_RADIUS: number_of_columns,
            }
        )
    )