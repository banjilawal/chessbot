# src/chess/arena/context/validator/exception/null.py

"""
Module: chess.arena.context.validator.exception.null
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_ARENA_CONTEXT EXCEPTION #======================#
    "NullArenaContextException",
]

from chess.system import NullException
from chess.arena import ArenaContextException


# ======================# NULL_ARENA_CONTEXT EXCEPTION #======================#
class NullArenaContextException(ArenaContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that ArenaContext validation failed because the candidate was null.

    # PARENT:
        *   NullArenaContextException
        *   ArenaContextValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_ARENA_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "ArenaContext validation failed: The candidate was null."