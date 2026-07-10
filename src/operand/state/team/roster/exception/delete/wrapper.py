__all__ = [
    # ======================# ROSTER_TOKEN_DELETION_FAILURE #======================#
    "TeamRosterTokenDeletionException",
]

from system import OperationException
from operand.state.team import TeamRosterException


# ======================# ROSTER_TOKEN_DELETION_FAILURE #======================#
class TeamRosterTokenDeletionException(TeamRosterException, OperationException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why deleting a Roster member fails. The encapsulated exceptions create
        chain for tracing the source of the failure.

    Super Class:
        *   TeamRosterException
        *   TransactionException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ROSTER_TOKEN_DELETION_FAILURE"
    MSG = "Roster occupant deletion failed."