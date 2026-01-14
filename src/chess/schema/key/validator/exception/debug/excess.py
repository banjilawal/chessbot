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
    # ========================= EXCESS_SCHEMA_KEYS_VALIDATION EXCEPTION =========================#
    "ExcessiveSchemaSuperKeysException",
]

# ========================= EXCESS_SCHEMA_KEYS_VALIDATION EXCEPTION =========================#
class ExcessiveSchemaSuperKeysException(SchemaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed SchemaSuperKey validation because more than one attribute was enabled.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSchemaSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESS_SCHEMA_KEYS_VALIDATION_ERROR"
    DEFAULT_MESSAGE = (
        "SchemaSuperKey validation failed: More than one attribute is not-null.Only ond attribute should be enabled."
    )