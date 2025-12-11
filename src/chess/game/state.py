# src/chess/game/state.py

"""
Module: chess.game.state
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto


class GameState(Enum):
    """
    # ROLE:  Lifecycle State, Transition State,

    # RESPONSIBILITIES:
    1.  States in a Game's lifecycle.

    # PARENT:
        *   Enum

    # PROVIDES:
    GameSnapshot

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    CREATED = auto(),
    RUNNING = auto(),
    ABORTED = auto(),
    TIED = auto(),
    WON = auto(),
    FAILURE = auto(),
    ROLLED_BACK = auto(),
    
    