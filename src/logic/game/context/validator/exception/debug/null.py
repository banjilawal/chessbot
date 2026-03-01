# src/logic/game/validator/exception/null.py

"""
Module: logic.game.validator.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_GAME_CONTEXT EXCEPTION #======================#
    "NullGameContextException",
]

from logic.system import NullException
from logic.game import InvalidGameContextException


# ======================# NULL_GAME_CONTEXT EXCEPTION #======================#
class NullGameContextException(InvalidGameContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that GameContext validation failed because the candidate was null.

    # PARENT:
        *   NullGameContextException
        *   InvalidGameContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_GAME_CONTEXT_EXCEPTION"
    MSG = "GameContext validation failed: The candidate was null."