# src/chess/schema/validator/exception/base.py

"""
Module: chess.schema.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.schema import SchemaException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# SCHEMA_VALIDATION_FAILURE EXCEPTION #======================#
    "SchemaValidationFailedException",
]

# ======================# SCHEMA_VALIDATION_FAILURE EXCEPTION #======================#
class SchemaValidationFailedException(SchemaException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Schema candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an SchemaValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The SchemaValidationFailedException chain is useful for tracing a  failure to its source.
    
    # PARENT:
        *   SchemaException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Schema validation failed."