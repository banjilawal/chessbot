# src/chess/board/state.py

"""
Module: chess.board.state
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from enum import Enum, auto


class BoardState(Enum):
    IS_EMPTY = auto(),
    HAS_BEEN_LAID_OUT = auto(),