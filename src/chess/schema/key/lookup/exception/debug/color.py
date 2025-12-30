# src/chess/schema/key/lookup/exception/debug/color.py

"""
Module: chess.schema.key.lookup.exception.debug.color
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.system import BoundsException
from chess.schema import SchemaException

__all__ = [
    # ======================# SCHEMA_COLOR_BOUNDS EXCEPTION #======================#
    "SchemaColorBoundsException",
]


# ======================# SCHEMA_COLOR_BOUNDS EXCEPTION #======================#
class SchemaColorBoundsException(SchemaException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Schema lookup failed because the color value was not permitted for the Schema attribute.
    
    # PARENT:
        *   BoundsException
        *   SchemaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COLOR_OUT_OF_SCHEMA_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "SchemaLookup failed: target was outside the set of permissible schema colors."
    
