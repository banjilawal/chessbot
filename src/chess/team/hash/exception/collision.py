# src/chess/team/hash/exception/collision.py

"""
Module: chess.team.hash.exception.collision
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_HASH_SCHEMA_COLLISION EXCEPTION #======================#
    "TeamSchemaCollisionException",
]


# ======================# TEAM_HASH_SCHEMA_COLLISION EXCEPTION #======================#
class TeamSchemaCollisionException(TeamHashException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if both teams in the hash have the same schema.

    # PARENT:
        *   TeamHashException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_HASH_SCHEMA_COLLISION_ERROR"
    DEFAULT_MESSAGE = "Both teams in the hash cannot have the same schema."