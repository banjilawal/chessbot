# src/chess/game/service/data/exception.py

"""
Module: chess.game.service.data.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


___all__ = [
    # ======================# GAME_DATA_SERVICE EXCEPTION #======================#
    "GameDataServiceException",
]

from chess.game import GameException
from chess.system import ServiceException


# ======================# GAME_DATA_SERVICE EXCEPTION #======================#
class GameDataServiceException(GameException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an GameListService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a GameListService method.

    # PARENT:
        *   ServiceException
        *   GameDataException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "GameListService raised an exception."