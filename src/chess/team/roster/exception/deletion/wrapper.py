__all__ = [
    # ======================# ROSTER_TOKEN_DELETION_FAILURE EXCEPTION #======================#
    "RosterTokenDeletionFailedException",
]

from chess.team import RosterServiceException


# ======================# ROSTER_TOKEN_DELETION_FAILURE EXCEPTION #======================#
class RosterTokenDeletionFailedException(RosterServiceException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Team.roster errors.


    # PARENT:
        *   RosterServiceException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ROSTER_TOKEN_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Roster token deletion failed."