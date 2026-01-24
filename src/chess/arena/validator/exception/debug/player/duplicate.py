# src/chess/arena/validator/exception/owner/duplicate.py

"""
Module: chess.arena.validator.exception.owner.duplicate
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.arena import ArenaDebugException

__all__ = [
    # ======================# DUPLICATE_PLAYER_IN_ARENA EXCEPTION #======================#
    "DuplicatePlayerInArenaException",
]


# ======================# DUPLICATE_PLAYER_IN_ARENA EXCEPTION #======================#
class DuplicatePlayerInArenaException(ArenaDebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a both unique teams in an Arena are owned by the same owner.

    # PARENT:
        *   ArenaDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DUPLICATE_PLAYER_IN_ARENA_ERROR"
    DEFAULT_MESSAGE = (
        "Both unique teams in an Arena are owned by the same owner. A owner is not allowed to play themselves."
    )