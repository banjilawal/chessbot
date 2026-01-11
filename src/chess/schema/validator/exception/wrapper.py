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
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a Schema. The encapsulated
        exceptions create a chain for tracing the source of the failure..
    
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