# src/chess/arena/validator/exception/player/duplicate.py

"""
Module: chess.game.arena.validator.exception.player.duplicate
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.arena import InvalidArenaException
from chess.agent import AddingDuplicateAgentException

__all__ = [
    # ======================# NULL ARENA EXCEPTION #======================#
    "DuplicatePlayerInArenaException",
]


# ======================# NULL ARENA EXCEPTION #======================#
class DuplicatePlayerInArenaException(InvalidArenaException, AddingDuplicateAgentException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a both unique teams in an Arena are owned by the same player.

    # PARENT:
        *   InvalidArenaException
        *   AddingDuplicatePlayerException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DUPLICATE_PLAYER_IN_ARENA_ERROR"
    DEFAULT_MESSAGE = (
        "Both unique teams in an Arena are owned by the same player. A player is not allowed to play themselves."
    )