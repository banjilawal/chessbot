# src/chess/schema/map/validator/exception/null.py

"""
Module: chess.schema.map.validator.exception.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.schema.map import InvalidSchemaSuperKeyException

__all__ = [
    # ======================# NULL_SCHEMA_SUPER_KEY EXCEPTION #======================#
    "NNullSchemaSuperKeyException",
]


# ======================# NULL_SCHEMA_SUPER_KEY EXCEPTION #======================#
class NNullSchemaSuperKeyException(InvalidSchemaSuperKeyException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an SchemaSuperKey validation candidate is null.
    2.  Raised if an entity, method or operation requires an SchemaSuperKey but receives null instead.

    # PARENT:
        *   NullException
        *   InvalidSchemaSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SCHEMA_SUPER_KEY_ERROR"
    DEFAULT_MESSAGE = "SchemaSuperKey cannot be null."