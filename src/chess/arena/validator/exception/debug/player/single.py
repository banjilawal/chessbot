# src/chess/arena/validator/exception/debug/player/single.py

"""
Module: chess.arena.validator.exception.debug.player.single
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import BoundsException
from chess.arena import ArenaDebugException

__all__ = [
    # ======================# SINGLE_PLAYER_IN_ARENA EXCEPTION #======================#
    "SinglePlayerInArena",
]


# ======================# SINGLE_PLAYER_IN_ARENA EXCEPTION #======================#
class SinglePlayerInArena(ArenaDebugException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an Arena's DatabaseService instance contains only one player.

    # PARENT:
        *   ArenaDebugException
        *   SinglePlayerInArena

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SINGLE_PLAYER_IN_ARENA_ERROR"
    DEFAULT_MESSAGE = (
        "Arena's UniquePlayerDataService contains only one player. A game cannot be played without only "
        "one player in the arena."
    )