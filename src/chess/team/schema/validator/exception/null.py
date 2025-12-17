# src/chess/team/schema/validator/exception/null.py

"""
Module: chess.team.schema.validator.exception.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.team import InvalidTeamSchemaException

__all__ = [
    #======================# TEAM_SCHEMA NULL EXCEPTIONS #======================#
    "NullTeamSchemaException",
]

#======================# TEAM_SCHEMA NULL EXCEPTIONS #======================#
class NullTeamSchemaException(InvalidTeamSchemaException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates an entity, method, or operation that required a TeamSchema got null instead.
    
    # PARENT:
        *   InvalidTeamSchemaException
        *   NullTeamSchemaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TEAM_SCHEMA_ERROR"
    DEFAULT_MESSAGE = "TeamSchema cannot be null."

    
    
    