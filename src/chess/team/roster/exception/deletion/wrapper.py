__all__ = [
    # ======================# ROSTER_MEMBER_DELETION_FAILURE EXCEPTION #======================#
    "RosterMemberDeletionFailedException",
]

from chess.team import TeamException


# ======================# ROSTER_MEMBER_DELETION_FAILURE EXCEPTION #======================#
class RosterMemberDeletionFailedException(TeamRo):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Team.roster errors.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ROSTER_MEMBER_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Roster member deletion failed."