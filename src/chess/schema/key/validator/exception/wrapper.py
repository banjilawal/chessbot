# src/chess/schema/key/validator/exception/wrapper.py

"""
Module: chess.schema.key.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaSuperKeyException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# SCHEMA_SUPER_KEY_VALIDATION_FAILURE EXCEPTION #======================#
    "SchemaSuperKeyValidationFailedException",
]


# ======================# SCHEMA_SUPER_KEY_VALIDATION_FAILURE EXCEPTION #======================#
class SchemaSuperKeyValidationFailedException(SchemaSuperKeyException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a SchemaSuperKey candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an SchemaSuperKeyValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The SchemaSuperKeyValidationFailedException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   SchemaSuperKeyException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_SUPER_KEY_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "SchemaSuperKey validation failed."