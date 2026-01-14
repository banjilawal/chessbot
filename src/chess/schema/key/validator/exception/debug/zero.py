# src/chess/schema/key/validator/exception/debug/flag/zero.py

"""
Module: chess.schema.key.validator.exception.debug.flag.zero
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaKeyException
from chess.system import ContextFlagCountException


__all__ = [
    # ========================= ZERO_SCHEMA_KEYS_VALIDATION EXCEPTION =========================#
    "ZeroSchemaKeysException",
]


# ========================= ZERO_SCHEMA_KEYS_VALIDATION EXCEPTION =========================#
class ZeroSchemaKeysException(SchemaKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a SchemaKey failed its safety certification because no attribute was enabled with a value.
    # 1.  Indicate that forward Schema lookup failed because all the SchemaKey attributes were null.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_SCHEMA_KEYS_VALIDATION_ERROR"
    DEFAULT_MESSAGE = (
        "SchemaKey validation failed: All attributes are null. A SchemaKey must have a "
        "single attribute enabled by a value."
    )