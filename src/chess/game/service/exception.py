# src/chess/game/service/exception/base.py

"""
Module: chess.game.service.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    #======================# GAME_SERVICE EXCEPTION #======================#
    "GameServiceException",
]


#======================# GAME_SERVICE EXCEPTION #======================#
class GameServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by GameService objects.
    2.  Raised when an exception hits the try-finally block of a GameService method.
    3.  Catchall for GameService failures that are not covered by a lower level GameService exception.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "GameService raised an exception."