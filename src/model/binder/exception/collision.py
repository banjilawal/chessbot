# src/model/binder/exception/collision.py

"""
Module: model.binder.exception.collision
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_BINDER_SCHEMA_COLLISION EXCEPTION #======================#
    "TeamSchemaCollisionException",
]

from model.team import TeamBinderException


# ======================# TEAM_BINDER_SCHEMA_COLLISION EXCEPTION #======================#
class TeamSchemaCollisionException(TeamBinderException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Raised if both teams in the binder have the same schema.

    Super Class:
        *   TeamBinderException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_BINDER_SCHEMA_COLLISION_EXCEPTION"
    MSG = "Both teams in the binder cannot have the same schema."