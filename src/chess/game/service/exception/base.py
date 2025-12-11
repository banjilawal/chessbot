# src/chess/game/service/exception/base.py

"""
Module: chess.game.service.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    #======================# GAME_SERVICE EXCEPTIONS #======================#
    "GameServiceException",
]


#======================# GAME_SERVICE EXCEPTIONS #======================#
class GameServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when an GameService's organic fields or methods run into a
        condition that leads to an operation failing.
    2.  Parent of exceptions raised by classes that highly cohere with GameService objects.
    3.  Catchall for GameService failure states that are not covered by a lower level
        GameService exception.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    GameServiceException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "GameService raised an exception."