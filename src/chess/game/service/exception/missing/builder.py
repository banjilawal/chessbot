# src/chess/game/service/exception/missing/builder.py

"""
Module: chess.game.service.exception.missing.builder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.game import InvalidGameServiceException

__all__ = [
    #======================# GAME_SERVICE EXCEPTIONS #======================#
    "MissingGameBuilderException",
]


#======================# GAME_SERVICE EXCEPTIONS #======================#
class MissingGameBuilderException(InvalidGameServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # PARENT:
        *   InvalidGameServiceException

    # RESPONSIBILITIES:
    1.  Indicate an GameService was constructed with either no GameBuilder or the wrong
        type of object.

    # PROVIDES:
    MissingGameBuilderException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "MISSING_GAME_BUILDER_ERROR"
    DEFAULT_MESSAGE = "GameService does not have the required GameBuilder."