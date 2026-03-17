# src/logic/team/hash/exception/black.py

"""
Module: logic.team.hash.exception.black
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# BLACK_TEAM_HAS_WRONG_SCHEMA EXCEPTION #======================#
    "BlackTeamHasWrongSchemaException",
]

from logic.team import TeamHashException


# ======================# BLACK_TEAM_HAS_WRONG_SCHEMA EXCEPTION #======================#
class BlackTeamHasWrongSchemaException(TeamHashException):
    """
    Role:Super Exception

    Responsibilities:
    1.  Indicates that the black team in the hash does not have a black schema.

    Super Class:
        *   TeamHashException

    Provides:

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "BLACK_TEAM_HAS_WRONG_SCHEMA_EXCEPTION"
    MSG = "Black Team does not have a black schema."