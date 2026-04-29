# src/config/board/dimension/config.py

"""
Module: config.board.dimension.config
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field

__all__ = [
    "NUMBER_OF_ROWS",
    "NUMBER_OF_COLUMNS",
    "BOARD_SIZE",
    "MIN_NAME_LENGTH",
    "MAX_NAME_LENGTH",
    "LONGEST_KNIGHT_LEG_SIZE",
    "BoardDimensionSetting",
]

from config import BoardProperty

NUMBER_OF_ROWS = 8
NUMBER_OF_COLUMNS = 8

BOARD_SIZE = 8
MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 40

LONGEST_KNIGHT_LEG_SIZE = 2


@dataclass
class BoardDimensionSetting:
    """
    Role
        -   Configuration Settings
  
    Responsibilities:
        1.  Default colors of board elements.
  
    Attributes:
  
    Provides:
  
    Super Class:
        Enum
    """
    table: Mapping[BoardProperty, int] = field(
        default_factory=lambda: MappingProxyType(
            {
                BoardProperty.DIMENSION: 8,
                BoardProperty.NUMBER_OF_ROWS: 8,
                BoardProperty.NUMBER_OF_COLUMNS: 8,
                BoardProperty.MAX_ROW_INDEX: 7,
                BoardProperty.MAX_COLUMN_INDEX: 7,
                BoardProperty.KNIGHT_RADIUS: 4,
            }
        )
    )