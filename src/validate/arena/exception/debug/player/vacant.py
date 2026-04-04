# src/logic/arena/validation/exception/debug/player/none.py

"""
Module: logic.arena.validation.exception.debug.player.none
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from logic.system import NullException
from logic.arena import ArenaDebugException

__all__ = [
    # ======================# NO_PLAYERS_IN_ARENA EXCEPTION #======================#
    "NoPlayersInArenaException",
]


# ======================# NO_PLAYERS_IN_ARENA EXCEPTION #======================#
class NoPlayersInArenaException(ArenaDebugException, NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Raised if an Arena's Database instance contains no players.

    Super Class:
        *   ArenaDebugException
        *   NoPlayersInArenaException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_PLAYERS_IN_ARENA_EXCEPTION"
    MSG = (
        "Arena's UniquePlayerDataService contains no players. A game cannot be played without two "
        "players in the arena."
    )