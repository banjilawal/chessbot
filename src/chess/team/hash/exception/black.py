# src/chess/team/hash/exception/black.py

"""
Module: chess.team.hash.exception.black
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# BLACK_TEAM_HAS_WRONG_SCHEMA EXCEPTION #======================#
    "BlackTeamHasWrongSchemaException",
]

from chess.team import TeamHashException


# ======================# BLACK_TEAM_HAS_WRONG_SCHEMA EXCEPTION #======================#
class BlackTeamHasWrongSchemaException(TeamHashException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicates that the black team in the hash does not have a black schema.

    # PARENT:
        *   TeamHashException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "BLACK_TEAM_HAS_WRONG_SCHEMA_ERROR"
    DEFAULT_MESSAGE = "Black Team does not have a black schema."