__all__ = [
    # ======================# ROSTER_TOKEN_DELETION_FAILURE #======================#
    "TeamRosterTokenDeletionException",
]

from logic.system import OperationException
from logic.team import TeamRosterException


# ======================# ROSTER_TOKEN_DELETION_FAILURE #======================#
class TeamRosterTokenDeletionException(TeamRosterException, OperationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why deleting a Roster member fails. The encapsulated exceptions create
        chain for tracing the source of the failure.

    # PARENT:
        *   TeamRosterException
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ROSTER_TOKEN_DELETION_FAILURE"
    MSG = "Roster occupant deletion failed."