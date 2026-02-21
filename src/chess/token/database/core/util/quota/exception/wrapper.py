__all__ = [
    # ======================# COUNT_OF_RANK_MEMBERS_FAILURE EXCEPTION #======================#
    "RankQuotaComputationFailedException",
]

from chess.token import RankQuotaManager, RankQuotaManagerException, TokenException
from chess.system import CalculationFailedException, ComputationFailedException


# ======================# COUNT_OF_RANK_MEMBERS_FAILURE EXCEPTION #======================#
class RankQuotaComputationFailedException(RankQuotaManagerException, ComputationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a count of records holding a rank did not succeed. The encapsulated
        exceptions create chain for tracing the source of the failure.

    # PARENT:
        *   TokenException
        *   ComputationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COUNT_OF_RANK_MEMBERS_FAILURE"
    DEFAULT_MESSAGE = "Count or rank members in Token list failed."