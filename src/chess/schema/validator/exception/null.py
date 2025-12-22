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
    # ======================# NULL_SCHEMA EXCEPTION #======================#
    "NullSchemaException",
]

#======================# NULL_SCHEMA EXCEPTION #======================#
class NullSchemaException(InvalidSchemaException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates an entity, method, or operation that required a Schema got null instead.
    
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
    ERROR_CODE = "NULL_SCHEMA_ERROR"
    DEFAULT_MESSAGE = "Schema cannot be null."

    
    
    