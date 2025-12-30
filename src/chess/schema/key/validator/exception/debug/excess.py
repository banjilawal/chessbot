# src/chess/schema/key/validator/exception/debug/excess.py

"""
Module: chess.schema.key.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaSuperKeyException
from chess.system import ContextFlagCountException

__all__ = [
    # ========================= EXCESS_SCHEMA_SUPER_KEYS_VALIDATION EXCEPTION =========================#
    "ExcessiveSchemaSuperKeysException",
]

# ========================= EXCESS_SCHEMA_SUPER_KEYS_VALIDATION EXCEPTION =========================#
class ExcessiveSchemaSuperKeysException(SchemaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a SchemaSuperKey failed its safety certification because more than one attribute was enabled
        with a value.
    # a forward Schema lookup failed because more than one SchemaSuperKey attribute was not null.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESS_SCHEMA_SUPER_KEYS_VALIDATION_ERROR"
    DEFAULT_MESSAGE = (
        "SchemaSuperKey validation failed: More than one attribute is not-null. A SchemaSuperKey can only have a "
        "single attribute enabled by a value."
    )