# src/chess/schema/key/validator/exception/wrapper.py

"""
Module: chess.schema.key.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaKeyException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# SCHEMA_KEY_VALIDATION_FAILURE EXCEPTION #======================#
    "SchemaKeyValidationFailedException",
]


# ======================# SCHEMA_KEY_VALIDATION_FAILURE EXCEPTION #======================#
class SchemaKeyValidationFailedException(SchemaKeyException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a SchemaKey candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an SchemaKeyValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The SchemaKeyValidationFailedException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   SchemaKeyException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_KEY_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "SchemaKey validation failed."