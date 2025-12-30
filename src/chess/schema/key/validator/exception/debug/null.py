# src/chess/schema/key/validator/exception/debug/null.py

"""
Module: chess.schema.key.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.schema import SchemaSuperKeyException

__all__ = [
    # ======================# NULL_SCHEMA_SUPER_KEY_VALIDATION EXCEPTION #======================#
    "NullSchemaSuperKeyException",
]


# ======================# NULL_SCHEMA_SUPER_KEY_VALIDATION EXCEPTION #======================#
class NullSchemaSuperKeyException(SchemaSuperKeyException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its SchemaSuperKey safety certification because it was null.

    # PARENT:
        *   NullException
        *   InvalidSchemaSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SCHEMA_SUPER_KEY_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "SchemaSuperKey validation failed: A SchemaSuperKey cannot be null."
