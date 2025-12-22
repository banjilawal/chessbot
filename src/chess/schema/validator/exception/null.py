# src/chess/schema/validator/exception/null.py

"""
Module: chess.schema.validator.exception.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.schema import InvalidSchemaException

__all__ = [
    # ======================# NULL_SCHEMA_VALIDATION EXCEPTION #======================#
    "NullSchemaException",
]


# ======================# NULL_SCHEMA_VALIDATION EXCEPTION #======================#
class NullSchemaException(InvalidSchemaException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its Schema safety certification because it was null.
    
    # PARENT:
        *   NullSchemaException
        *   InvalidSchemaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SCHEMA_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Schema validation failed: A Schema cannot be null."