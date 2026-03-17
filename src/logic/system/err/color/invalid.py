# src/logic/system/err/color/invalid.py

"""
Module: logic.system.err.color.invalid
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.system import GameColorException, ValidationException

__all__ = [
#======================# GAME_COLOR_VALIDATION EXCEPTION #======================#
    "InvalidGameColorException",
]

#======================# GAME_COLOR_VALIDATION EXCEPTION #======================#
class InvalidGameColorException(GameColorException, ValidationException):
    """
    Role:Exception Wrapper

    Responsibilities:
    1.  Indicate a candidate failed a GameColor validation test.
    2.  Wrap an exception that hits the try-finally block of a SchemKeyValidator method.

    Super Class:
        *   GameColorException
        *   ValidationException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "GAME_COLOR_VALIDATION_EXCEPTION"
    MSG = "GameColor validation failed."