# src/chess/system/err/color.py

"""
Module: chess.system.err.color
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import InvalidGameColorException, NullException

__all__ = [
    # ======================# NULL_GAME_COLOR_VALIDATION EXCEPTION #======================#
    "NullGameColorException",
]
# ======================# NULL_GAME_COLOR_VALIDATION EXCEPTION #======================#
class NullGameColorException(InvalidGameColorException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its GameColor safety certification because it was null.

    # PARENT:
        *   NullSchemaException
        *   InvalidSchemaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_GAME_COLOR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "GameColor validation failed: A GameColor cannot be null."