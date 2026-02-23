__all__ = [
    # ======================# ROSTER_TOKEN_DELETION_FAILURE #======================#
    "TeamRosterTokenDeletionException",
]

from chess.system import OperationException
from chess.team import TeamRosterException


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
    ERROR_CODE = "ROSTER_TOKEN_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Roster occupant deletion failed."