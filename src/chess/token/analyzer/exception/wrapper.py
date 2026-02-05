__all__ = [
    # ======================# ROSTER_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
    "TokenReadniessAnalysisFailedException",
]

from chess.system import AnalysisFailedException
from chess.token import TokenStateException


# ======================# ROSTER_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
class TokenReadniessAnalysisFailedException(TokenStateException, AnalysisFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the occupant's state has been evaluated.

    # PARENT:
        *   WrapperException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ROSTER_RELATION_ANALYSIS_FAILURE"
    DEFAULT_MESSAGE = "RosterRelationTest failed."