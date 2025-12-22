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
    # ========================= EXCESSIVE_GAME_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveGameContextFlagsException"
]


# ========================= EXCESSIVE_GAME_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveGameContextFlagsException(InvalidGameContextException, ContextFlagCountException):
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
    ERROR_CODE = "EXCESSIVE_GAME_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = (
        "Excessive GameContext flags were set. an Game search can only use one-and-only "
        "map flag at a time."
    )
