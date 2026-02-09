# src/chess/team/hash/exception/white.py

"""
Module: chess.team.hash.exception.white
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# WHITE_TEAM_HAS_WRONG_SCHEMA EXCEPTION #======================#
    "WhiteTeamHasWrongSchemaException",
]

from chess.team import TeamHashException


# ======================# WHITE_TEAM_HAS_WRONG_SCHEMA EXCEPTION #======================#
class WhiteTeamHasWrongSchemaException(TeamHashException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicates that the white team in the hash does not have a white schema.

    # PARENT:
        *   TeamHashException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "WHITE_TEAM_HAS_WRONG_SCHEMA_ERROR"
    DEFAULT_MESSAGE = "White Team does not have a white schema."