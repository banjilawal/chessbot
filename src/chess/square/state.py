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
    CONCRETE_OCCUPANT = auto(),
    GHOST_NOT_PURGED= auto()