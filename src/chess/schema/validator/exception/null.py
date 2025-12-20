# src/chess/schema/number_bounds_validator/exception/null.py

"""
Module: chess.schema.number_bounds_validator.exception.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.schema import InvalidSchemaException

__all__ = [
    #======================# _SCHEMA NULL EXCEPTION #======================#
    "NullSchemaException",
]

#======================# SCHEMA NULL EXCEPTION #======================#
class NullSchemaException(InvalidSchemaException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates an entity, method, or operation that required a Schema got null instead.
    
    # PARENT:
        *   InvalidSchemaException
        *   NullSchemaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL__SCHEMA_ERROR"
    DEFAULT_MESSAGE = "Schema cannot be null."

    
    
    