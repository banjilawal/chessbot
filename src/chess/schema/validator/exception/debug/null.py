# src/chess/schema/validator/exception/null.py

"""
Module: chess.schema.validator.exception.null
Author: Banji Lawal
Created: 2025-12-16
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_SCHEMA EXCEPTION #======================#
    "NullSchemaException",
]

from chess.system import NullException
from chess.schema import SchemaDebugException


# ======================# NULL_SCHEMA EXCEPTION #======================#
class NullSchemaException(SchemaDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the validation candidate was null.

    # PARENT:
        *   SchemaDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SCHEMA_ERROR"
    DEFAULT_MESSAGE = "Schema validation failed: The validation candidate cannot be null."