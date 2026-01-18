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
    SINGLE_OCCUPANT = auto(),
    TOKEN_ENTERING = auto(),
    DEPARTING_TOKEN = auto(),
    DOUBLE_COMBATANT_OCCUPANCY = auto()