# src/chess/token/model/state.py

"""
Module: chess.token.model.state
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto

class TokenBoardState(Enum):
    NEVER_PLACED = auto(),
    FORMED_ON_BOARD = auto(),
    REMOVED_FROM_BOARD = auto(),