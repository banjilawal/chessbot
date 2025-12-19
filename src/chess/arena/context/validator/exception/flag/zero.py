# src/chess/arena/context/validator/exception/flag/zero.py

"""
Module: chess.arena.context.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.system import BoundsException
from chess.arena import InvalidArenaContextException

__all__ = [
    # ========================= ZERO_ARENA_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroArenaContextFlagsException"
]


# ========================= ZERO_ARENA_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroArenaContextFlagsException(InvalidArenaContextException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates no ArenaContext flag was enabled. One and only one Arena attribute-value tuple is required for
        a search.

    # PARENT:
        *   BoundsException
        *   InvalidArenaContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_ARENA_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "Zero ArenaContext flags were set. One and only one context flag must be enabled,"