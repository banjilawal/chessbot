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
    # ======================# SCHEMA_SUPER_KEY EXCEPTION #======================#
    "SchemaSuperKeyException",
]


# ======================# SCHEMA_SUPER_KEY EXCEPTION #======================#
class SchemaSuperKeyException(SchemaException, ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for conditions which are not covered by SchemaSuperKeyException subclasses.

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
    ERROR_CODE = "SCHEMA_SUPER_KEY_ERROR"
    DEFAULT_ERROR_CODE = "SchemaSuperKey raised an exception."