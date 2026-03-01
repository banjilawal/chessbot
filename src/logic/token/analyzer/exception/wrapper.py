__all__ = [
    # ======================# ROSTER_RELATION_ANALYSIS_FAILURE #======================#
    "TokenReadniessAnalysisException",
]

from logic.system import AnalysisException
from logic.token import TokenStateException


# ======================# ROSTER_RELATION_ANALYSIS_FAILURE #======================#
class TokenReadniessAnalysisException(TokenStateException, AnalysisException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the occupant's state has been evaluated.

    # PARENT:
        *   WorkerException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ROSTER_RELATION_ANALYSIS_FAILURE"
    MSG = "RosterRelationTest failed."