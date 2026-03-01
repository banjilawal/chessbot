# src/logic/game/validator/exception/flag/zero.py

"""
Module: logic.game.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from logic.system import ContextFlagCountException
from logic.game import InvalidGameContextException

__all__ = [
    # ========================= ZERO_GAME_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroGameContextFlagsException"
]


# ========================= ZERO_GAME_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroGameContextFlagsException(InvalidGameContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  no GameContext flag was enabled. One and only one Game attribute-value-tuple is required for
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
    ERR_CODE = "ZERO_GAME_CONTEXT_FLAGS_EXCEPTION"
    MSG = (
        "Zero GameContext flags were set. Cannot search for Games if one-and_oly-one "
        "map flag is enabled."
    )
