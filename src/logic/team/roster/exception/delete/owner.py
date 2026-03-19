from logic.team import TeamRosterException

__all__ = [
    # ======================# ENEMY_CANNOT_JOIN_ROSTER EXCEPTION #======================#
    "CannotDeleteTokenFromDifferentRosterException",
]


# ======================# ENEMY_CANNOT_JOIN_ROSTER EXCEPTION #======================#
class CannotDeleteTokenFromDifferentRosterException(TeamRosterException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Indicate that inserting into a Team's roster failed because it the occupant had a different team.

    Super Class:
        *   TeamRosterException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ENEMY_CANNOT_JOIN_ROSTER"
    MSG = "Adding roster member failed: The occupant is on an enemy team."