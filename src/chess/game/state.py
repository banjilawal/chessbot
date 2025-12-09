# src/chess/game/state.py

"""
Module: chess.game.state
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto


class GameState(Enum):
    CREATED = auto(),
    RUNNING = auto(),
    ABORTED = auto(),
    TIED = auto(),
    WON = auto(),
    FAILURE = auto(),
    
    