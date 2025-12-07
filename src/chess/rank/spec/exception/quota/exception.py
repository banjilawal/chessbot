# src/chess/rank/spec/exception/quota/base.py

"""
Module: chess.rank.spec.exception.quota.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import RankSpecException
from chess.system import BoundsException, NullException, ValidationException

__all__ = [
    # ======================# TEAM_QUOTA EXCEPTION SUPER CLASS #======================#
    "TeamQuotaException",
    # ======================# NULL TEAM_QUOTA EXCEPTIONS #======================#
    "InvalidTeamQuotaException",
    # ======================# NULL TEAM_QUOTA EXCEPTIONS #======================#
    "NullTeamQuotaException",
    # ======================# TEAM_QUOTA BOUNDS EXCEPTIONS #======================#
    "TeamQuotaBoundsException",
]


# ======================# TEAM_QUOTA EXCEPTION SUPER CLASS #======================#
class TeamQuotaException(RankSpecException):
    """
    Super class of exceptions raised by Rank.team_quota objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "TEAM_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Rank.team_quota raised an exception."


# ======================# TEAM_QUOTA VALIDATION EXCEPTION #======================#
class InvalidTeamQuotaException(TeamQuotaException, ValidationException):
    """Raised if a TeamQuotaValidation candidate fails a check."""
    ERROR_CODE = "TEAM_QUOTA_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Rank.team_quota validation failed."


# ======================# NULL TEAM_QUOTA EXCEPTION #======================#
class NullTeamQuotaException(TeamQuotaException, NullException):
    """Raised if the Rank.team_quota is null."""
    ERROR_CODE = "NULL_TEAM_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Rank.team_quota cannot be null."


# ======================# TEAM_QUOTA BOUNDS EXCEPTIONS #======================#
class TeamQuotaBoundsException(TeamQuotaException, BoundsException):
    """Raised if the quota is not in RankSpec."""
    ERROR_CODE = "TEAM_QUOTA_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The team_quota is not included in the RankSpec settings."