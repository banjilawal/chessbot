# src/chess/schema/map/exception.py

"""
Module: chess.schema.map.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaException
from chess.system import ContextException


__all__ = [
    # ======================# SCHEMA_MAP EXCEPTION #======================#
    "SchemaMapException",
]


# ======================# SCHEMA_MAP EXCEPTION #======================#
class SchemaMapException(SchemaException, ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by SchemaMap objects.
    2.  Catchall for conditions which are not covered by lower level SchemaMap exception.

    # PARENT:
        *   SchemaException
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_MAP_ERROR"
    DEFAULT_ERROR_CODE = "SchemaMap raised an exception."