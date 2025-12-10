# src/chess/game/service/data/exception/invalid.py

"""
Module: chess.game.service.data.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.game import GameDataServiceException
from chess.system import ValidationFailedException


__all__ = [
    #======================# GAME_DATA_SERVICE VALIDATION EXCEPTIONS #======================#
    "InvalidGameDataServiceException",
]

#======================# GAME_DATA_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidGameDataServiceException(GameDataServiceException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during GameDataService verification process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an GameDataServiceValidator method.

    # PARENT
        *   GameDataServiceException
        *   ValidationFailedException

    # PROVIDES:
    InvalidGameDataServiceException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_DATA_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "GameDataService validation failed."