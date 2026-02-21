# src/chess/schema/validator/exception/base.py

"""
Module: chess.schema.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.schema import SchemaException
from chess.system import ValidationException

__all__ = [
    # ======================# SCHEMA_VALIDATION_FAILURE EXCEPTION #======================#
    "SchemaValidationException",
]

# ======================# SCHEMA_VALIDATION_FAILURE EXCEPTION #======================#
class SchemaValidationException(SchemaException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Schema. The exception chain traces the ultimate source of failure..
    
    # PARENT:
        *   SchemaException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Schema validation failed."