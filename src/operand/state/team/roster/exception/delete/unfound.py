__all__ = [
    # ======================# ROSTER_MEMBER_TO_REMOVE_DOES_NOT_EXIST EXCEPTION #======================#
    "TeamRosterMemberDoesNotExistForRemovalException",
]

from operand.state.team import TeamRosterException


# ======================# ROSTER_MEMBER_TO_REMOVE_DOES_NOT_EXIST EXCEPTION #======================#
class TeamRosterMemberDoesNotExistForRemovalException(TeamRosterException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that the roster member could not be removed because it does not exist.

    Super Class:
        *   TeamDaaServiceException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ROSTER_MEMBER_TO_REMOVE_DOES_NOT_EXIST_EXCEPTION"
    MSG = "Token deletion failed: The roster member does not exist. Nothing to remove."