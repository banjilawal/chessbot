# src/chess/team/finder/exception/debug/id.py

"""
Module: chess.team.finder.exception.debug.id
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

__all__ = [
    "TeamSearchIdCollisionException",
]

from chess.team import Team
from chess.system import CollisionException


# ======================# TEAM_SEARCH_ID_COLLISION EXCEPTION #======================#
class TeamSearchIdCollisionException(Team, CollisionException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That search by Team.id which should produce either a single match or none returned
        different teams with the same id.

    # PARENT:
        *   TeamException
        *   CollisionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SEARCH_ID_COLLISION_ERROR"
    DEFAULT_MESSAGE = (
        "TeamSearch failed: There was id collision. The results contain different teams that share an id."
    )