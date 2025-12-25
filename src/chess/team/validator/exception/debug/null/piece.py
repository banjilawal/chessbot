__all__ = [
    # ======================# NULL_TEAM EXCEPTION #======================#
    "NullTeamException",
]

from chess.system import NullException
from chess.team import TeamException


# ======================# NULL_ EXCEPTION #======================#
class NullPieceDataServiceException(TeamException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Team certification one of its UniqueDataService
        instances was null.

    # PARENT:
        *   NullException
        *   TeamException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TEAM_ERROR"
    DEFAULT_MESSAGE = "Team validation failed: The candidate was null."