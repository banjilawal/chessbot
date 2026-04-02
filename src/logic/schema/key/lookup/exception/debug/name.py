# src/logic/schema/key/lookup/exception/debug/stack.py

"""
Module: logic.schema.key.lookup.exception.debug.stack
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

__all__ = [
    # ======================# SCHEMA_NAME_BOUNDS EXCEPTION #======================#
    "SchemaNameBoundsException",
]

from logic.schema import SchemaException
from logic.system import BoundsException


# ======================# SCHEMA_NAME_BOUNDS EXCEPTION #======================#
class SchemaNameBoundsException(SchemaException, BoundsException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a Schema lookup failed because the stack was not a key to any Schema variant.

    Super Class:
        *   BoundsException
        *   SchemaException
  
    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SCHEMA_NAME_BOUNDS_EXCEPTION"
    MSG = "SchemaLookupProcess failed: No schema entries use the target as their key."
