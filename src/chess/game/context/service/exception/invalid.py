# src/chess/game/context/service/exception/invalid.py

"""
Module: chess.game.context.service.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.game import GameContextServiceException


__all__ = [
    # ======================# GAME_CONTEXT_SERVICE VALIDATION EXCEPTIONS #======================#
    "InvalidGameContextServiceException",
]


# ======================# GAME_CONTEXT_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidGameContextServiceException(GameContextServiceException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during GameContextService verification process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an GameContextServiceValidator method.
    
    # PARENT
        *   GameContextServiceException
        *   ValidationFailedException

    # PROVIDES:
    InvalidGameContextServiceException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_CONTEXT_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "GameContextService validation failed."