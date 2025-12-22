# src/chess/game/service/data/unique/exception.py

"""
Module: chess.game.service.data.unique.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.game import GameException
from chess.system import UniqueDataServiceException

__all__ = [
    # ======================# UNIQUE_GAME_DATA_SERVICE EXCEPTION #======================#
    "UniqueGameDataServiceException",
]


# ======================# UNIQUE_GAME_DATA_SERVICE EXCEPTION #======================#
class UniqueGameDataServiceException(GameException, UniqueDataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by UniqueGameDataService objects.
    2.  Wraps an exception that hits the try-finally block of an UniqueDataGame's method.

    # PARENT:
        *   GameException
        *   UniqueDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_GAME_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueGameDataService raised an exception."