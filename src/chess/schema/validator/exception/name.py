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
    # ======================# SCHEMA_NAME_BOUNDS EXCEPTION #======================#
    "SchemaNameBoundsException",
]


# ======================# SCHEMA_NAME_BOUNDS EXCEPTION #======================#
class SchemaNameBoundsException(InvalidSchemaException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that no variant of Schema has that name.

    # PARENT:
        *   NameException
        *   BoundsException
        *   InvalidSchemaException
  
    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "There is no Schema variant with that name."
