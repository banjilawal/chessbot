# src/chess/schema/validator/exception/base.py

"""
Module: chess.schema.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.schema import InvalidSchemaException
from chess.system import BoundsException, GameColorException

__all__ = [
    # ======================# SCHEMA COLOR BOUNDS EXCEPTIONS #======================#
    "SchemaColorBoundsException",
]


# ======================# SCHEMA COLOR BOUNDS EXCEPTIONS #======================#
class SchemaColorBoundsException(InvalidSchemaException, BoundsException, GameColorException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a color is outside the range of acceptable Schema colors.

    # PARENT:
        *   InvalidSchemaException
        *   BoundsException
        *   GameColorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_GAME_COLOR_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "GameColor is not included in the set of permissible schema colors."
