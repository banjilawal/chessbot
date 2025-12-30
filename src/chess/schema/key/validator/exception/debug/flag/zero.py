# src/chess/schema/key/validator/exception/debug/flag/zero.py

"""
Module: chess.schema.key.validator.exception.debug.flag.zero
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaSuperKeyException
from chess.system import ContextFlagCountException


__all__ = [
    # ========================= ZERO_SCHEMA_SUPER_KEYS_VALIDATION EXCEPTION =========================#
    "ZeroSchemaSuperKeysException",
]


# ========================= ZERO_SCHEMA_SUPER_KEYS_VALIDATION EXCEPTION =========================#
class ZeroSchemaSuperKeysException(SchemaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a SchemaSuperKey failed its safety certification because no attribute was enabled with a value.
    # 1.  Indicate that forward Schema lookup failed because all the SchemaSuperKey attributes were null.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_SCHEMA_SUPER_KEYS_VALIDATION_ERROR"
    DEFAULT_MESSAGE = (
        "SchemaSuperKey validation failed: All attributes are null. A SchemaSuperKey must have a "
        "single attribute enabled by a value."
    )