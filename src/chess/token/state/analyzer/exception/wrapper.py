__all__ = [
    # ======================# ROSTER_RELATION_TEST_FAILURE EXCEPTION #======================#
    "TokenStateAnalysisFailedException",
]

from chess.system import RelationAnalysisFailedException
from chess.token import TokenStateException


# ======================# ROSTER_RELATION_TEST_FAILURE EXCEPTION #======================#
class TokenStateAnalysisFailedException(TokenStateException, RelationAnalysisFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the token's state has been evaluated.

    # PARENT:
        *   WrapperException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ROSTER_RELATION_TEST_FAILURE"
    DEFAULT_MESSAGE = "RosterRelationTest failed."