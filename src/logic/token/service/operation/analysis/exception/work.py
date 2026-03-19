__all__ = [
    # ======================# ROSTER_RELATION_ANALYSIS_FAILURE #======================#
    "TokenReadinessAnalysisException",
]

from logic.system import AnalysisException, RelationAnalysisException
from logic.token import TokenStateException


# ======================# ROSTER_RELATION_ANALYSIS_FAILURE #======================#
class TokenReadinessAnalysisException(RelationAnalysisException):
    """
    Role:Exception Work, Encapsulation, Error Chaining

    Responsibilities:
    1.  Wrap any exception that kills the relation test process before the occupant's state has been evaluated.

    Super Class:
        *   WorkException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ROSTER_RELATION_ANALYSIS_FAILURE"
    MSG = "RosterRelationTest failed."