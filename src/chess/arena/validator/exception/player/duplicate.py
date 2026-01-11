# src/chess/arena/validator/exception/player/duplicate.py

"""
Module: chess.arena.validator.exception.player.duplicate
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.arena import ArenaValidationFailedException
from chess.agent import AddingDuplicateAgentException

__all__ = [
    # ======================# NULL ARENA EXCEPTION #======================#
    "DuplicatePlayerInArenaException",
]


# ======================# NULL ARENA EXCEPTION #======================#
class DuplicatePlayerInArenaException(ArenaValidationFailedException, AddinDuplicateItemException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a both unique teams in an Arena are owned by the same player.

    # PARENT:
        *   ArenaValidationFailedException
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