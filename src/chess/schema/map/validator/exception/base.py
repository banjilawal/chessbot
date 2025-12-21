# src/chess/schema/map/validator/exception/base.py

"""
Module: chess.schema.map.validator.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaMapException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# SCHEMA_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidSchemaMapException",
]


# ======================# SCHEMA_CONTEXT VALIDATION SUPER CLASS #======================#
class InvalidSchemaMapException(SchemaMapException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised SchemaMap validation.
    2.  Wraps unhandled exception that hit the finally-block in SchemaMapValidator methods.

    # PARENT:
        *   SchemaMapException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "SchemaMap validation failed."