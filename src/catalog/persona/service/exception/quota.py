# src/logic/persona/service/exception/quota.py

"""
Module: logic.persona.service.exception.quota
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# RANK_QUOTA_PER_TEAM_LOOKUP_FAILURE #======================#
    "RankQuotaPerTeamLookupFailedException",
]

from model.token import TokenException
from system import CalculationFailedException


# ======================# RANK_QUOTA_PER_TEAM_LOOKUP_FAILURE #======================#
class RankQuotaPerTeamLookupFailedException(TokenException, CalculationFailedException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions that indicate looking up the max number of rank members per team. The encapsulated
        exceptions create chain for tracing the source of the failure.

    Super Class:
        *   TokenException
        *   ComputationException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "RANK_QUOTA_PER_TEAM_LOOKUP_FAILURE"
    MSG = "Looking up how many team members can hold a rank failed."