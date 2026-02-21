# src/chess/game/database/exception.py

"""
Module: chess.game.database.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.game import GameException
from chess.system import DatabaseException

__all__ = [
    # ======================# UNIQUE_GAME_STACK_SERVICE EXCEPTION #======================#
    "UniqueGameDataServiceException",
]


# ======================# UNIQUE_GAME_STACK_SERVICE EXCEPTION #======================#
class UniqueGameDataServiceException(GameException, DatabaseException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exception raised by UniqueGameDataService objects.
    2.  Wraps an exception that hits the try-finally block of an UniqueDataGame's method.

    # PARENT:
        *   GameException
        *   DatabaseException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_GAME_STACK_ERROR"
    DEFAULT_MESSAGE = "UniqueGameDataService raised an exception."