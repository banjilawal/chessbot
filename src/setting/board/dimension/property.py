# src/setting/board/dimension/property.py

"""
Module: setting.board.dimension.property
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from enum import Enum, auto


class BoardProperty(Enum):
    DIMENSION = auto(),
    NUMBER_OF_ROWS = auto(),
    NUMBER_OF_COLUMNS = auto(),
    MAX_ROW_INDEX = auto(),
    MAX_COLUMN_INDEX = auto(),
    KNIGHT_RADIUS = auto(),