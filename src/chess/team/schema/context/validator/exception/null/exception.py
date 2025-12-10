# src/chess/team/schema/context/validator/exception/null/exception.py

"""
Module: chess.team.schema.validator.null.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.team import InvalidTeamSchemaContextException

__all__ = [
    # ======================# TEAMSCHEMA_CONTEXT NULL EXCEPTIONS #======================#
    "NullTeamSchemaContextException",
]


# ======================# TEAMSCHEMA_CONTEXT NULL EXCEPTIONS #======================#
class NullTeamSchemaContextException(InvalidTeamSchemaContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an TeamSchemaContext validation candidate is null.
    2.  Raised if an entity, method or operation requires an TeamSchemaContext but receives null instead.

    # PARENT:
        *   InvalidTeamSchemaContextException
        *   NullTeamSchemaContextException

    # PROVIDES:
        *   NullTeamSchemaContextException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TEAMSCHEMA_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamSchemaContext cannot be null."