__all__ = [
    # ======================# ROSTER_MEMBER_TO_REMOVE_DOES_NOT_EXIST EXCEPTION #======================#
    "RosterMemberDoesNotExistForRemovalException",
]

from chess.team import RosterServiceException


# ======================# ROSTER_MEMBER_TO_REMOVE_DOES_NOT_EXIST EXCEPTION #======================#
class RosterMemberDoesNotExistForRemovalException(RosterServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that the roster member could not be removed because it does not exist.

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ROSTER_MEMBER_TO_REMOVE_DOES_NOT_EXIST_ERROR"
    DEFAULT_MESSAGE = "Token deletion failed: The roster member does not exist. Nothing to remove."