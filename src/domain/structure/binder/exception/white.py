# src/domain/structure/binder/exception/white.py

"""
Module: domain.structure.binder.exception.white
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# WHITE_TEAM_HAS_WRONG_ARCHETYPE EXCEPTION #======================#
    "WhiteTeamHasWrongArchetypeException",
]

from domain.structure.team import TeamBinderException


# ======================# WHITE_TEAM_HAS_WRONG_ARCHETYPE EXCEPTION #======================#
class WhiteTeamHasWrongArchetypeException(TeamBinderException):
    """
    Role:Super Exception

    Responsibilities:
    1.  Indicates that the white team in the binder does not have a white archetype.

    Super Class:
        *   TeamBinderException

    Provides:

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "WHITE_TEAM_HAS_WRONG_ARCHETYPE_EXCEPTION"
    MSG = "White Team does not have a white archetype."