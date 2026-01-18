# src/chess/square/state.py

"""
Module: chess.square.state
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto


class SquareState(Enum):
    EMPTY = auto(),
    OCCUPIED = auto(),
    GHOST_OCCUPATION = auto()