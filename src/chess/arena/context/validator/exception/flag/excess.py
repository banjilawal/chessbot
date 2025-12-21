# src/chess/arena/map/validator/exception/flag/excess.py

"""
Module: chess.arena.map.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.arena import InvalidArenaContextException

__all__ = [
    # ========================= EXCESSIVE_ARENA_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveArenaContextFlagsException"
]


# ========================= EXCESSIVE_ARENA_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveArenaContextFlagsException(InvalidArenaContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates more than one ArenaContext flag was enabled. Only one Arena attribute-value-tuple can be used in
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidArenaContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_ARENA_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = (
        "Excessive ArenaContext flags were set. an Arena search can only use one-and-only "
        "map flag at a time."
    )