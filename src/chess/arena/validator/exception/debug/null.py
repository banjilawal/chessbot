# src/chess/arena/validator/exception/null.py

"""
Module: chess.arena.validator.exception.null
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_ARENA EXCEPTION #======================#
    "NullArenaException",
]

from chess.system import NullException
from chess.arena import ArenaDebugException


# ======================# NULL_ARENA EXCEPTION #======================#
class NullArenaException(ArenaDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the candidate was null.

    # PARENT:
        *   ArenaDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_ARENA_ERROR"
    MSG = "Arena validation failed: The candidate cannot be null."