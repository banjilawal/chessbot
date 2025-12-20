# src/chess/game/number_bounds_validator/exception/null.py

"""
Module: chess.game.number_bounds_validator.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.game import InvalidGameException

__all__ = [
    # ======================# GAME_ NULL EXCEPTION #======================#
    "NullGameException",
]


# ======================# NULL GAME EXCEPTION #======================#
class NullGameException(InvalidGameException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a Game validation candidate is null.
    2.  Raised if an entity, method or operation requires a Game but receives null instead.

    # PARENT:
        *   InvalidGameException
        *   NullGameException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_GAME__ERROR"
    DEFAULT_MESSAGE = "Game cannot be null."


