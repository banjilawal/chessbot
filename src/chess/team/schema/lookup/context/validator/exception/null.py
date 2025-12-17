# src/chess/team/schema/context/validator/exception/null/exception.py

"""
Module: chess.team.schema.context.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.team import InvalidSchemaContextException

__all__ = [
    # ======================# TEAM_SCHEMA_CONTEXT NULL EXCEPTIONS #======================#
    "NullSchemaContextException",
]


# ======================# TEAM_SCHEMA_CONTEXT NULL EXCEPTIONS #======================#
class NullSchemaContextException(InvalidSchemaContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an SchemaContext validation candidate is null.
    2.  Raised if an entity, method or operation requires an SchemaContext but receives null instead.

    # PARENT:
        *   InvalidSchemaContextException
        *   NullException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TEAM_SCHEMA_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "SchemaContext cannot be null."