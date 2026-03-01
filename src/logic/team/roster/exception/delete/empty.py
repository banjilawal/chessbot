__all__ = [
    # ======================# POPPING_EMPTY_ROSTER EXCEPTION #======================#
    "PoppingEmptyTeamRosterException",
]

from logic.team import TeamRosterException


# ======================# POPPING_EMPTY_ROSTER EXCEPTION #======================#
class PoppingEmptyTeamRosterException(TeamRosterException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a roster member failed because the roster was empty.

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_EMPTY_ROSTER_EXCEPTION"
    MSG = "Roster member deletion failed: The roster is empty. Nothing to delete."