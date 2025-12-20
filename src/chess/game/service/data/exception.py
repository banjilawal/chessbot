# src/chess/game/service/data/exception.py

"""
Module: chess.game.service.data.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.game import GameException
from chess.system import DataServiceException

__all__ = [
    # ======================# GAME_DATA_SERVICE EXCEPTION #======================#
    "GameDataServiceException",
]


# ======================# GAME_DATA_SERVICE EXCEPTION #======================#
class GameDataServiceException(GameException, DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by GameDataService objects.
    2.  Raised when an exception hits the try-finally block of a GameDataService method.
    3.  Catchall for GameDataService failures that are not covered by a lower level GameDataService exception.

    # PARENT:
        *   GameException
        *   DataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_DATA_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "GameDataService raised an exception."