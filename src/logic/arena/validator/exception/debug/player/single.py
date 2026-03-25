# src/logic/arena/validation/exception/debug/player/single.py

"""
Module: logic.arena.validation.exception.debug.player.single
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from logic.system import BoundsException
from logic.arena import ArenaDebugException

__all__ = [
    # ======================# SINGLE_PLAYER_IN_ARENA EXCEPTION #======================#
    "SinglePlayerInArena",
]


# ======================# SINGLE_PLAYER_IN_ARENA EXCEPTION #======================#
class SinglePlayerInArena(ArenaDebugException, BoundsException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Raised if an Arena's Database instance contains only one player.

    Super Class:
        *   ArenaDebugException
        *   SinglePlayerInArena

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SINGLE_PLAYER_IN_ARENA_EXCEPTION"
    MSG = (
        "Arena's UniquePlayerDataService contains only one player. A game cannot be played without only "
        "one player in the arena."
    )