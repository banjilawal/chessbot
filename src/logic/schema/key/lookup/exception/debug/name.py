# src/logic/schema/key/lookup/exception/debug/name.py

"""
Module: logic.schema.key.lookup.exception.debug.name
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
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Schema lookup failed because the name was not a key to any Schema variant.

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
    ERR_CODE = "SCHEMA_NAME_BOUNDS_EXCEPTION"
    MSG = "SchemaLookup failed: No schema entries use the target as their key."
