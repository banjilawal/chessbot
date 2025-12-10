# src/chess/game/service/data/exception/exception.py

"""
Module: chess.game.service.data.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import DataServiceException

__all__ = [
    #======================# GAME_DATA_SERVICE EXCEPTIONS #======================#
    "GameDataServiceException",
]


#======================# GAME_DATA_SERVICE EXCEPTIONS #======================#
class GameDataServiceException(DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by GameDataService objects.
    2.  Parent of exceptions raised by classes that highly cohere with GameDataService objects.
    3.  Catchall for GameDataService failure states that are not covered by a lower level
        GameDataService exception.

    # PARENT
        *   DataServiceException

    # PROVIDES:
    GameDataServiceException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_DATA_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "GameDataService raised an exception."