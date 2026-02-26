# src/chess/game/validator/exception/flag/excess.py

"""
Module: chess.game.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.game import InvalidGameContextException

__all__ = [
    # ========================= ARENA_GAME_CONTEXT_FLAG EXCEPTION =========================#
    "ArenaGameContextFlagsException"
]


# ========================= ARENA_GAME_CONTEXT_FLAG EXCEPTION =========================#
class ArenaGameContextFlagsException(InvalidGameContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  more than one GameContext flag was enabled. Only one Game attribute-value-tuple can be used in
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidGameContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ARENA_GAME_CONTEXT_FLAG_ERROR"
    MSG = (
        "Arena GameContext flags were set. an Game search can only use one-and-only "
        "map flag at a time."
    )
