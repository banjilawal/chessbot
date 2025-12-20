# src/chess/arena/context/exception.py

"""
Module: chess.arena.context.exception
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.arena import ArenaException
from chess.system import ContextException

__all__ = [
    # ======================# ARENA_CONTEXT EXCEPTION #======================#
    "ArenaContextException",
]


# ======================# ARENA_CONTEXT EXCEPTION #======================#
class ArenaContextException(ArenaException, ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by ArenaContext objects.
    2.  Catchall for conditions which are not covered by lower level ArenaContext exceptions.

    # PARENT:
        *   ArenaException
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "ArenaContext raised an exception."

