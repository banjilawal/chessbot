# src/logic/schema/key/validation/exception/debug/null.py

"""
Module: logic.schema.key.validation.exception.debug.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from system import NullException
from catalog.schema import SchemaKeyException

__all__ = [
    # ======================# NULL_SCHEMA_KEY_VALIDATION EXCEPTION #======================#
    "NullSchemaKeyException",
]


# ======================# NULL_SCHEMA_KEY_VALIDATION EXCEPTION #======================#
class NullSchemaKeyException(SchemaKeyException, NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a rank failed its SchemaKey safety certification because it was null.

    Super Class:
        *   NullException
        *   InvalidSchemaKeyException

    Provides:

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_SCHEMA_KEY_VALIDATION_EXCEPTION"
    MSG = "SchemaKey validation failed: A SchemaKey cannot be null."
