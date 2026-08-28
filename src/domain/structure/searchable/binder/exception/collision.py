# src/domain/structure/binder/exception/collision.py

"""
Module: domain.structure.binder.exception.collision
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_BINDER_ARCHETYPE_COLLISION EXCEPTION #======================#
    "TeamArchetypeCollisionException",
]

from domain.structure.team import TeamBinderException


# ======================# TEAM_BINDER_ARCHETYPE_COLLISION EXCEPTION #======================#
class TeamArchetypeCollisionException(TeamBinderException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Raised if both teams in the binder have the same archetype.

    Super Class:
        *   TeamBinderException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_BINDER_ARCHETYPE_COLLISION_EXCEPTION"
    MSG = "Both teams in the binder cannot have the same archetype."