# src/chess/arena/validator/exception/debug/player/none.py

"""
Module: chess.arena.validator.exception.debug.player.none
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import NullException
from chess.arena import ArenaDebugException

__all__ = [
    # ======================# NO_PLAYERS_IN_ARENA EXCEPTION #======================#
    "NoPlayersInArenaException",
]


# ======================# NO_PLAYERS_IN_ARENA EXCEPTION #======================#
class NoPlayersInArenaException(ArenaDebugException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an Arena's Database instance contains no players.

    # PARENT:
        *   ArenaDebugException
        *   NoPlayersInArenaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_PLAYERS_IN_ARENA_ERROR"
    DEFAULT_MESSAGE = (
        "Arena's UniquePlayerDataService contains no players. A game cannot be played without two "
        "players in the arena."
    )