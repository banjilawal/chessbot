# src/logic/schema/key/lookup/exception/debug/color.py

"""
Module: logic.schema.key.lookup.exception.debug.color
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from system import BoundsException
from model.catalog import SchemaException

__all__ = [
    # ======================# SCHEMA_COLOR_BOUNDS EXCEPTION #======================#
    "SchemaColorBoundsException",
]


# ======================# SCHEMA_COLOR_BOUNDS EXCEPTION #======================#
class SchemaColorBoundsException(SchemaException, BoundsException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a Schema lookup failed because the color value was not permitted for the Schema attribute.
    
    Super Class:
        *   BoundsException
        *   SchemaException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "COLOR_OUT_OF_SCHEMA_BOUNDS_EXCEPTION"
    MSG = "SchemaLookupProcess failed: target was outside the set of permissible schema colors."
    
