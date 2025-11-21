# src/chess/rank/validator/quota/collision.py

"""
Module: chess.rank.validator.quota.exceptiom
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.system import NullException
from chess.rank import InvalidRankException


__all__ = [
    "RankQuotaException",
    
    # ======================# NULL RANK_QUOTA EXCEPTIONS #======================#
    "NullRankQuotaException",
    
    # ======================# RANK_QUOTA BOUNDS EXCEPTIONS #======================#
    "RankQuotaBelowBoundsException",
    "RankQuotaAboveBoundsException",
    
    # ======================# RANK_QUOTA_INCONSISTENCY EXCEPTIONS #======================#
    "KingQuotaException",
    "QueenQuotaException",
    "BishopQuotaException",
    "RookQuotaException",
    "KnightQuotaException",
    "PawnQuotaException",
]


class RankQuotaException(InvalidRankException):
    """
    Super class of exceptions raised by Quota objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Rank.team_quota raised an exception."


# ======================# NULL RANK_QUOTA EXCEPTIONS #======================#
class NullRankQuotaException(RankQuotaException, NullException):
    """Raised if the Rank.team_quota is null. This should never happen. It might indicate data inconsistency."""
    ERROR_CODE = "NULL_RANK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Rank.team_quota cannot be null."


# ======================# RANK_QUOTA BOUNDS EXCEPTIONS #======================#
class RankQuotaBelowBoundsException(RankQuotaException):
    """Raised if the team_quota zero or less. The lowest team_quota is 1."""
    ERROR_CODE = "RANK_QUOTA_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Rank.team_quota cannot be less than one."


class RankQuotaAboveBoundsException(RankQuotaException):
    """Raised if the team_quota higher than the Pawn's."""
    ERROR_CODE = "NULL_RANK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Rank.team_quota cannot be null. There may be a data inconsistency or system failure."
    
    
# ======================# RANK_QUOTA INCONSISTENCY EXCEPTIONS #======================#
class KingQuotaException(RankQuotaException):
    """Raised when the team_quota assigned to a King differs from the RankSpec value."""
    ERROR_CODE = "_QUEEN_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Queen team_quota."


class QueenQuotaException(RankQuotaException):
    """Raised when the team_quota assigned to a Queen differs from the RankSpec value."""
    ERROR_CODE = "QUEEN_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Queen team_quota."


class RookQuotaException(RankQuotaException):
    """Raised when the team_quota assigned to a Rook differs from the RankSpec value."""
    ERROR_CODE = "ROOK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Rook team_quota."


class BishopQuotaException(RankQuotaException):
    """Raised when the team_quota assigned to a Bishop differs from the RankSpec value."""
    ERROR_CODE = "BISHOP_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Bishop team_quota."


class KnightQuotaException(RankQuotaException):
    """Raised when the team_quota assigned to a Knight differs from the RankSpec value."""
    ERROR_CODE = "KNIGHT_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Knight team_quota."


class PawnQuotaException(RankQuotaException):
    """Raised when the team_quota assigned to a Pawn differs from the RankSpec value."""
    ERROR_CODE = "PAWN_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Pawn team_quota."
