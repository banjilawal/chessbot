# src/chess/team/team_schema/context/exception.py

"""
Module: chess.team.team_schema.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextException


__all__ = [
    # ======================# TEAM_SCHEMA_CONTEXT EXCEPTION SUPER CLASS #======================#
    "TeamSchemaContextException",
]



# ======================# TEAM_SCHEMA_CONTEXT EXCEPTION SUPER CLASS #======================#
class TeamSchemaContextException(ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by TeamSchemaContext objects.
    2.  Catchall for conditions which are not covered by lower level TeamSchemaContext exceptions.

    # PARENT:
        *   ContextException

    # PROVIDES:
    TeamSchemaContextException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SCHEMA_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "TeamSchemaContext raised an exception."