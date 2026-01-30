# src/chess/token/service/data/exception/calculation/rank/count.py

"""
Module: chess.token.service.data.exception.calculation.rank.count
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# COUNT_OF_RANK_MEMBERS_FAILURE EXCEPTION #======================#
    "RankCountCalculationFailedException",
]

from chess.token import TokenException
from chess.system import CalculationFailedException


# ======================# COUNT_OF_RANK_MEMBERS_FAILURE EXCEPTION #======================#
class RankCountCalculationFailedException(TokenException, CalculationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a count of records holding a rank did not succeed. The encapsulated
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