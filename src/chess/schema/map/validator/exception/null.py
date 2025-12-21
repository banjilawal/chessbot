# src/chess/schema/map/validator/exception/null.py

"""
Module: chess.schema.map.validator.exception.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.schema import InvalidSchemaMapException

__all__ = [
    # ======================# SCHEMA_CONTEXT NULL EXCEPTION #======================#
    "NullSchemaMapException",
]


# ======================# SCHEMA_CONTEXT NULL EXCEPTION #======================#
class NullSchemaMapException(InvalidSchemaMapException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an SchemaMap validation candidate is null.
    2.  Raised if an entity, method or operation requires an SchemaMap but receives null instead.

    # PARENT:
        *   NullException
        *   InvalidSchemaMapException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SCHEMA_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "SchemaMap cannot be null."