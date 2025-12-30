# src/chess/schema/key/lookup/exception/debug/name.py

"""
Module: chess.schema.key.lookup.exception.debug.name
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

__all__ = [
    # ======================# SCHEMA_NAME_BOUNDS EXCEPTION #======================#
    "SchemaNameBoundsException",
]

from chess.schema import SchemaException
from chess.system import BoundsException


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
    ERROR_CODE = "SCHEMA_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "SchemaLookup failed: No schema entries use the target as their key."
