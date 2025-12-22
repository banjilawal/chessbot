# src/chess/schema/key/validator/exception/flag/zero.py

"""
Module: chess.schema.key.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.schema import InvalidSchemaSuperKeyException


__all__ = [
    # ========================= ZERO_SCHEMA_SUPER_KEYS EXCEPTION =========================#
    "ZeroSchemaSuperKeysException",
]


# ========================= ZERO_SCHEMA_SUPER_KEYS EXCEPTION =========================#
class ZeroSchemaSuperKeysException(InvalidSchemaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  a forward Schema lookup failed because all the SchemaSuperKey attributes were null.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_SCHEMA_SUPER_KEYS_ERROR"
    DEFAULT_MESSAGE = (
        "All SchemaSuperKey fields are null. One-and-only-one SchemaSuperKey attribute must be set to "
        "run a forward Schema lookup."
    )