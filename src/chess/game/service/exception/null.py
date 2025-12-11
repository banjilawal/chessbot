# src/chess/game/service/exception/null.py

"""
Module: chess.game.service.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.game import InvalidGameServiceException


__all__ = [
    "NullGameServiceException",
]


#======================# NULL GAME_SERVICE EXCEPTION #======================#
class NullGameServiceException(InvalidGameServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an GameService but got null instead.

    # PARENT:
        *   InvalidGameServiceException
        *   NullException

    # PROVIDES:
    NullGameServiceException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_GAME_SERVICE_ERROR"
    DEFAULT_MESSAGE = "GameService cannot be null."
