# src/chess/arena/context/number_bounds_validator/exception/null.py

"""
Module: chess.arenaContext.arena.context.number_bounds_validator.exception.null
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import NullException
from chess.arena import InvalidArenaContextException

__all__ = [
    # ======================# NULL_ARENA_CONTEXT EXCEPTION #======================#
    "NullArenaContextException",
]


# ======================# NULL_ARENA_CONTEXT EXCEPTION #======================#
class NullArenaContextException(InvalidArenaContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a ArenaContext validation candidate is null.
    2.  Raised if an entity, method or operation requires a ArenaContext but receives null instead.

    # PARENT:
        *   NullArenaContextException
        *   InvalidArenaContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_ARENA_CONTEXT__ERROR"
    DEFAULT_MESSAGE = "ArenaContext cannot be null."
