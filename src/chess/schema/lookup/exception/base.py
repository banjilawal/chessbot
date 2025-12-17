# src/chess/team/schema/lookup/exception/base.py

"""
Module: chess.team.schema.lookup.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ServiceException
from chess.team import TeamSchemaException


__all__ = [
    # ======================# TEAM_SCHEMA_LOOKUP EXCEPTION #======================#
    "TeamSchemaLookupException",
]


# ======================# TEAM_SCHEMA_LOOKUP EXCEPTION #======================#
class TeamSchemaLookupException(TeamSchemaException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by TeamSchemaLookup objects.
    2.  Raised when no specific exception exists for the error interrupting TeamSchemaLookup's
        processes from their normal flows.

    # PARENT:
        *   TeamSchemaException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_LOOKUP_ERROR"
    DEFAULT_MESSAGE = "TeamLookup raised an exception."