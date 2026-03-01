# src/logic/schema/key/validator/exception/debug/excess.py

"""
Module: logic.schema.key.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from logic.schema import SchemaKeyException
from logic.system import ContextFlagCountException

__all__ = [
    # ========================= EXCESS_SCHEMA_KEYS_VALIDATION EXCEPTION =========================#
    "ArenaSchemaKeysException",
]

# ========================= EXCESS_SCHEMA_KEYS_VALIDATION EXCEPTION =========================#
class ArenaSchemaKeysException(SchemaKeyException, ContextFlagCountException):
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
    ERR_CODE = "EXCESS_SCHEMA_KEYS_VALIDATION_EXCEPTION"
    MSG = (
        "SchemaKey validation failed: More than one attribute is not-null.Only ond attribute should be enabled."
    )