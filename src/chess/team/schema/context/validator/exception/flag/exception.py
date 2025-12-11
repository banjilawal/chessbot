# src/chess/team/schema/context/validator/exception/flag/exception.py

"""
Module: chess.team.schema.validator.flag.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.team import InvalidTeamSchemaContextException

__all__ = [
    # ========================= NO_TEAM_SCHEMA_CONTEXT_FLAG EXCEPTION =========================#
    "NoTeamSchemaContextFlagException",
    # ========================= TOO_MANY_TEAM_SCHEMA_CONTEXT_FLAGS EXCEPTION =========================#
    "TooManyTeamSchemaContextFlagsException"
]


# ========================= NO_TEAM_SCHEMA_CONTEXT_FLAG EXCEPTION =========================#
class NoTeamSchemaContextFlagException(InvalidTeamSchemaContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no TeamSchemaContext flag is provided with a searcher value.

    # PARENT:
        *   InvalidTeamSchemaContextException
        *   ContextFlagCountException

    # PROVIDES:
        *   NoTeamSchemaContextFlagException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_TEAM_SCHEMA_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "No TeamSchemaContext flag was selected. A context flag must be turned on with a target value."


# ========================= TOO_MANY_TEAMS_CHEMA_CONTEXT_FLAGS EXCEPTION =========================#
class TooManyTeamSchemaContextFlagsException(InvalidTeamSchemaContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, TeamSchemaContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one TeamSchema attribute is going to be used in an TeamSchemaFinder.

    # PARENT:
        *   InvalidTeamSchemaContextException
        *   ContextFlagCountException

    # PROVIDES:
        *   TooManyTeamSchemaContextFlagsException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOO_MANY_TEAM_SCHEMA_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one TeamSchemaContext flag was selected. Only one context flag is allowed."