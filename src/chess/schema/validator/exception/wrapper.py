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
    "InvalidSchemaException",
]


# ======================# SCHEMA_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidSchemaException(SchemaException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate a candidate failed a Schema validation test.
    2.  Wrap an exception that hits the try-finally-block in SchemaValidator methods.

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
    ERROR_CODE = "SCHEMA_VALIDATION_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Schema validation failed."
