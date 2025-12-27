# src/chess/team/finder/exception/debug/id.py

"""
Module: chess.team.finder.exception.debug.id
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

__all__ = [
    # ======================# ARENA_DUPLICATE_SCHEMA EXCEPTION #======================#
    "ArenaDuplicateSchemaException",
]

from chess.arena import ArenaException


# ======================# ARENA_DUPLICATE_SCHEMA EXCEPTION #======================#
class ArenaDuplicateSchemaException(ArenaException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that both teams in an arena have the same schema.

    # PARENT:
        *   ArenaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_DUPLICATE_SCHEMA_ERROR"
    DEFAULT_MESSAGE = (
        "The Arena has two teams with the same schema."
    )