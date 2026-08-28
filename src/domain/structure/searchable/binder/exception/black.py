# src/domain/structure/binder/exception/black.py

"""
Module: domain.structure.binder.exception.black
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# BLACK_TEAM_HAS_WRONG_ARCHETYPE EXCEPTION #======================#
    "BlackTeamHasWrongArchetypeException",
]



# ======================# BLACK_TEAM_HAS_WRONG_ARCHETYPE EXCEPTION #======================#
class BlackTeamHasWrongArchetypeException(TeamBinderException):
    """
    Role:Super Exception

    Responsibilities:
    1.  Indicates that the black team in the binder does not have a black archetype.

    Super Class:
        *   TeamBinderException

    Provides:

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "BLACK_TEAM_HAS_WRONG_ARCHETYPE_EXCEPTION"
    MSG = "Black Team does not have a black archetype."