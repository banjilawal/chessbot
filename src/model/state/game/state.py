# src/model/state/game/state.py

"""
Module: model.state.game.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class GameState(Enum):
    """
    Role: Lifecycle State, Transition State,

    Responsibilities:
    1.  States in a Game's lifecycle.

    Super Class:
        *   Enum

    # PROVIDES:
    Snapshot


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
    
    