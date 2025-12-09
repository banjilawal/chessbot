# src/chess/game/validator/exception/null/exception.py

"""
Module: chess.game.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.game import InvalidGameException

__all__ = [
    #======================# GAME NULL EXCEPTIONS #======================#
    "NullGameException",
]

#======================# GAME_CONTEXT NULL EXCEPTIONS #======================#
class NullGameException(InvalidGameException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an Game  but got null instead.

    # PARENT
        *   InvalidGameException
        *   NullException

    # PROVIDES:
    NullGameCException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_GAME_ERROR"
    DEFAULT_MESSAGE = "Game cannot be null."
