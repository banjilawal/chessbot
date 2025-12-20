# src/chess/schema/validator/exception/color.py

"""
Module: chess.schema.validator.exception.color
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.schema import InvalidSchemaException
from chess.system import BoundsException, GameColorException

__all__ = [
    # ======================# SCHEMA_COLOR_BOUNDS EXCEPTION #======================#
    "SchemaColorBoundsException",
]


# ======================# SCHEMA_COLOR_BOUNDS EXCEPTION #======================#
class SchemaColorBoundsException(InvalidSchemaException, BoundsException, GameColorException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate a color is not in the set of acceptable Schema colors.

    # PARENT:
        *   BoundsException
        *   GameColorException
        *   InvalidSchemaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COLOR_OUT_OF_SCHEMA_BOUNDS_ERROR"
    DEFAULT_MESSAGE = (
        "The color is not in the set of permissible schema colors. There is no schema "
        "entry associated with this color."
    )
    
