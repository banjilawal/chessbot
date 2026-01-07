# src/chess/team/roster/exception/insertion/quota.py

"""
Module: chess.team.roster.exception.insertion.quota
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_RANK_QUOTA_FULL EXCEPTION #======================#
    "TeamRankQuotaFullException",
]
    
from chess.team import TeamException

# ======================# TEAM_RANK_QUOTA_FULL EXCEPTION #======================#
class TeamRankQuotaFullException(TeamRosterException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a token cannot be added to roster because berths are full.

    # PARENT:
        *   TeamException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_RANK_QUOTA_FULL_ERROR"
    DEFAULT_MESSAGE = "Adding roster member failed: quota for the rank is full."