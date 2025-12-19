# src/chess/game/service/data/unique/exception/base.py

"""
Module: chess.game.service.data.unique.exception.base
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
    1.  Parent of exceptions raised by UniqueGameDataService objects.
    2.  Raised when an exception hits the try-finally block of a UniqueGameDataService method.
    3.  Catchall for UniqueGameDataService failures that are not covered by a lower level UniqueGameDataService exceptions.

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
    DEFAULT_ERROR_CODE = "UniqueGameDataService raised an exception."