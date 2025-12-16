# src/chess/game/service/data/exception/null.py

"""
Module: chess.game.service.data.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.game import InvalidGameDataServiceException


__all__ = [
    "GameDataServiceNullException",
]


#======================# NULL GAME_DATA_SERVICE EXCEPTION #======================#
class GameDataServiceNullException(InvalidGameDataServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an GameDataService but got null instead.

    # PARENT:
        *   InvalidGameDataServiceException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_GAME_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "GameDataService cannot be null."