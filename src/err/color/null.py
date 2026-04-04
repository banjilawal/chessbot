# src/logic/system/err/color/null.py

"""
Module: logic.system.err.color.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from system import GameColorException, NullException

__all__ = [
    # ======================# NULL_GAME_COLOR_VALIDATION EXCEPTION #======================#
    "NullGameColorException",
]
# ======================# NULL_GAME_COLOR_VALIDATION EXCEPTION #======================#
class NullGameColorException(GameColorException, NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a rank failed its GameColor safety certification because it was null.

    Super Class:
        *   NullSchemaException
        *   InvalidSchemaException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_GAME_COLOR_VALIDATION_EXCEPTION"
    MSG = "GameColor validation failed: A GameColor cannot be null."