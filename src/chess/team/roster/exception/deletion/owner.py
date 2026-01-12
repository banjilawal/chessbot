from chess.team import RosterServiceException

__all__ = [
    # ======================# ENEMY_CANNOT_JOIN_ROSTER EXCEPTION #======================#
    "CannotDeleteTokenRosterDoesNotOwnException",
]


# ======================# ENEMY_CANNOT_JOIN_ROSTER EXCEPTION #======================#
class CannotDeleteTokenRosterDoesNotOwnException(RosterServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that inserting into a Team's roster failed because it the token had a different team.

    # PARENT:
        *   RosterServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ENEMY_CANNOT_JOIN_ROSTER"
    DEFAULT_MESSAGE = "Adding roster member failed: The token is on an enemy team."