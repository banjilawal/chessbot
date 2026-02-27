# src/chess/arena/validator/exception/flag/excess.py

"""
Module: chess.arena.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.arena import ArenaContextException

__all__ = [
    # ========================= AEXCESS)RENA_ARENA_CONTEXT_FLAGS EXCEPTION =========================#
    "ExcessArenaContextFlagsException"
]


# ========================= EXCESS_ARENA_ARENA_CONTEXT_FLAGS EXCEPTION =========================#
class ExcessArenaContextFlagsException(ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  more than one ArenaContext flag was enabled. Only one Arena attribute-value-tuple can be used in
        a search.

    # PARENT:
        *   ContextFlagCountException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "EXCESS_ARENA_ARENA_CONTEXT_FLAGS_EXCEPTION"
    MSG = (
        "Arena ArenaContext flags were set. an Arena search can only use one-and-only "
        "map flag at a time."
    )