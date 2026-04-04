# src/model/team/hash/exception/collision.py

"""
Module: model.team.hash.exception.collision
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_HASH_SCHEMA_COLLISION EXCEPTION #======================#
    "TeamSchemaCollisionException",
]

from model.team import TeamHashException


# ======================# TEAM_HASH_SCHEMA_COLLISION EXCEPTION #======================#
class TeamSchemaCollisionException(TeamHashException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Raised if both teams in the hash have the same schema.

    Super Class:
        *   TeamHashException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_HASH_SCHEMA_COLLISION_EXCEPTION"
    MSG = "Both teams in the hash cannot have the same schema."