# src/chess/schema/key/validator/exception/debug/null.py

"""
Module: chess.schema.key.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.schema import SchemaKeyException

__all__ = [
    # ======================# NULL_SCHEMA_KEY_VALIDATION EXCEPTION #======================#
    "NullSchemaKeyException",
]


# ======================# NULL_SCHEMA_KEY_VALIDATION EXCEPTION #======================#
class NullSchemaKeyException(SchemaKeyException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its SchemaKey safety certification because it was null.

    # PARENT:
        *   NullException
        *   InvalidSchemaKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SCHEMA_KEY_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "SchemaKey validation failed: A SchemaKey cannot be null."
