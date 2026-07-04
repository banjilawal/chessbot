__all__ = [
    # ======================# POPPING_EMPTY_ROSTER EXCEPTION #======================#
    "PoppingEmptyTeamRosterException",
]

from model.state.team import TeamRosterException


# ======================# POPPING_EMPTY_ROSTER EXCEPTION #======================#
class PoppingEmptyTeamRosterException(TeamRosterException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to remove a roster member failed because the roster was empty.

    Super Class:
        *   TeamDaaServiceException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_EMPTY_ROSTER_EXCEPTION"
    MSG = "Roster member deletion failed: The roster is empty. Nothing to delete."