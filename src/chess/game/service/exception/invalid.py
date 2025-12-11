# src/chess/game/service/exception/invalid.py

"""
Module: chess.game.service.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.game import GameServiceException


__all__ = [
    #======================# GAME_SERVICE VALIDATION EXCEPTIONS #======================#
    "InvalidGameServiceException",
]

#======================# GAME_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidGameServiceException(GameServiceException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during GameService verification process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an GameServiceValidator method.

    # PARENT:
        *   GameServiceException
        *   ValidationFailedException

    # PROVIDES:
    InvalidGameServiceException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "GameService validation failed."