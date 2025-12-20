# src/chess/schema/context/validator/exception/null.py

"""
Module: chess.schema.context.validator.exception.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.schema import InvalidSchemaContextException

__all__ = [
    # ======================# SCHEMA_CONTEXT NULL EXCEPTION #======================#
    "NullSchemaContextException",
]


# ======================# SCHEMA_CONTEXT NULL EXCEPTION #======================#
class NullSchemaContextException(InvalidSchemaContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an SchemaContext validation candidate is null.
    2.  Raised if an entity, method or operation requires an SchemaContext but receives null instead.

    # PARENT:
        *   NullException
        *   InvalidSchemaContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SCHEMA_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "SchemaContext cannot be null."