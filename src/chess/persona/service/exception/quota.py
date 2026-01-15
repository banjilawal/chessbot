# src/chess/persona/service/exception/quota.py

"""
Module: chess.persona.service.exception.quota
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# RANK_QUOTA_PER_TEAM_LOOKUP_FAILURE #======================#
    "RankQuotaPerTeamLookupFailedException",
]

from chess.token import TokenException
from chess.system import CalculationFailedException


# ======================# RANK_QUOTA_PER_TEAM_LOOKUP_FAILURE #======================#
class RankQuotaPerTeamLookupFailedException(TokenException, CalculationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate looking up the max number of rank members per team. The encapsulated
        exceptions create chain for tracing the source of the failure.

    # PARENT:
        *   TokenException
        *   CalculationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "RANK_QUOTA_PER_TEAM_LOOKUP_FAILURE"
    DEFAULT_MESSAGE = "Looking up how many team members can hold a rank failed."