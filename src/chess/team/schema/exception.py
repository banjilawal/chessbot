# src/chess/team/schema/exception.py

"""
Module: chess.team.schema.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.team import TeamException


__all__ = [
    # ======================# TEAM_SCHEMA EXCEPTION #======================#
    "TeamSchemaException",
]


# ======================# TEAM_SCHEMA EXCEPTION #======================#
class TeamSchemaException(TeamException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by TeamSchema objects.
    2.  Catchall for conditions which are not covered by lower level TeamSchema exceptions.

    # PARENT:
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SCHEMA_ERROR"
    DEFAULT_ERROR_CODE = "TeamSchema raised an exception."