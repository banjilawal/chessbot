# src/chess/game/service/exception.py

"""
Module: chess.game.service.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException
from chess.game import GameException

__all__ = [
    # ======================# GAME_SERVICE EXCEPTION #======================#
    "GameServiceException",
]


# ======================# GAME_SERVICE EXCEPTION #======================#
class GameServiceException(GameException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an GameService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a GameService method.

    # PARENT:
        *   ServiceException
        *   GameException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_SERVICE_ERROR"
    DEFAULT_MESSAGE = "GameService raised an exception."