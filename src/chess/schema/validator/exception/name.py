# src/chess/schema/validator/exception/name.py

"""
Module: chess.schema.validator.exception.name
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.schema import InvalidSchemaException
from chess.system import BoundsException, NameException

__all__ = [
    # ======================# SCHEMA NAME BOUNDS EXCEPTIONS #======================#
    "SchemaNameBoundsException",
]


# ======================# SCHEMA NAME BOUNDS EXCEPTIONS #======================#
class SchemaNameBoundsException(InvalidSchemaException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a string is outside the range of acceptable Schema names.

    # PARENT:
        *   InvalidSchemaException
        *   BoundsException
        *   NameException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Name is not included in the set of permissible schema names."