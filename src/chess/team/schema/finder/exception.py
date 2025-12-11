# src/chess/team/schema/finder/exception.py

"""
Module: chess.team.schema.finder.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import FinderException

__all__ = [
    # ======================# TEAMSCHEMA_FINDER EXCEPTIONS #======================#
    "TeamSchemaFinderException",
]


# ======================# TEAM_SCHEMA_FINDER EXCEPTIONS #======================#
class TeamSchemaFinderException(FinderException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by TeamSchemaFinder objects
    2.  Wraps unhandled exceptions that hit the try-finally block of an TeamSchemaFactory method.

    # PARENT
        *   FinderException

    # PROVIDES:
        *   TeamSchemaFinderException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SCHEMA_FINDER_ERROR"
    DEFAULT_MESSAGE = "TeamSchemaFinder raised an exception."