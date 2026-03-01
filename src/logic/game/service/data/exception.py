# src/logic/game/database/core/exception.py

"""
Module: logic.game.database.core.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


___all__ = [
    # ======================# GAME_STACK_SERVICE EXCEPTION #======================#
    "GameDataServiceException",
]

from logic.game import GameException
from logic.system import ServiceException


# ======================# GAME_STACK_SERVICE EXCEPTION #======================#
class GameDataServiceException(GameException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an GameStackService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a GameStackService method.

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
    ERR_CODE = "GAME_STACK_EXCEPTION"
    MSG = "GameStackService raised an exception."