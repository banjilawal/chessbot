# src/chess/token/database/core/util/quota/exception/wrapper.py

"""
Module: chess.token.database.core.util.quota.exception.wrapper
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# RANK_QUOTA_ANALYSIS_FAILURE #======================#
    "RankQuotaAnalysisException",
]

from chess.system import ComputationException


# ======================# RANK_QUOTA_ANALYSIS_FAILURE #======================#
class RankQuotaAnalysisException(ComputationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why rank quota analysis on a token_stack failed. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   ComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "RANK_QUOTA_ANALYSIS_FAILURE"
    DEFAULT_MESSAGE = "Rank quota analysis failed."