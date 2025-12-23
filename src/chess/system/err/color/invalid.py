# src/chess/system/err/color.py

"""
Module: chess.system.err.color
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import GameColorException, ValidationFailedException

__all__ = [
#======================# GAME_COLOR_VALIDATION EXCEPTION #======================#
    "InvalidGameColorException",
]

#======================# GAME_COLOR_VALIDATION EXCEPTION #======================#
class InvalidGameColorException(GameColorException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate a candidate failed a GameColor validation test.
    2.  Wrap an exception that hits the try-finally block of a SchemSuperKeyValidator method.

    # PARENT:
        *   GameColorException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_COLOR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "GameColor validation failed."