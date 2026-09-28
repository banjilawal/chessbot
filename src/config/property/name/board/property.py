# src/config/property/name/board/property.py

"""
Module: config.property.name.board.property
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class BoardPropertyName(Enum):
    """
     Role:
        1.  Configuration
        2.  Metadata

     Responsibilities:
         1. Names of BoardProperty attribute.

     Attributes:

     Provides:

     Super Class:
        Enum
     """
    CELL_COUNT = auto(),
    NUMBER_OF_ROWS = auto(),
    NUMBER_OF_COLUMNS = auto(),
    MAX_ROW_INDEX = auto(),
    MAX_COLUMN_INDEX = auto(),
    DIAGONAL_LENGTH = auto()
    TEAM_SIZE = auto()