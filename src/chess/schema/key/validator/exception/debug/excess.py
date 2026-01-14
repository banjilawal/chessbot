# src/chess/schema/key/validator/exception/debug/excess.py

"""
Module: chess.schema.key.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaKeyException
from chess.system import ContextFlagCountException

__all__ = [
    # ========================= EXCESS_SCHEMA_KEYS_VALIDATION EXCEPTION =========================#
    "ExcessiveSchemaKeysException",
]

# ========================= EXCESS_SCHEMA_KEYS_VALIDATION EXCEPTION =========================#
class ExcessiveSchemaKeysException(SchemaKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed SchemaKey validation because more than one attribute was enabled.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESS_SCHEMA_KEYS_VALIDATION_ERROR"
    DEFAULT_MESSAGE = (
        "SchemaKey validation failed: More than one attribute is not-null.Only ond attribute should be enabled."
    )