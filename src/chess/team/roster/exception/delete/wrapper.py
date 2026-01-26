__all__ = [
    # ======================# ROSTER_TOKEN_DELETION_FAILURE EXCEPTION #======================#
    "TeamRosterTokenDeletionFailedException",
]

from chess.system import OperationFailedException
from chess.team import TeamRosterException


# ======================# ROSTER_TOKEN_DELETION_FAILURE EXCEPTION #======================#
class TeamRosterTokenDeletionFailedException(TeamRosterException, OperationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why deleting a Roster member fails. The encapsulated exceptions create
        chain for tracing the source of the failure.

    # PARENT:
        *   TeamRosterException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ROSTER_TOKEN_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Roster occupant deletion failed."