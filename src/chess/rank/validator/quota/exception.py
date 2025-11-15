# src/chess/rank/validator/quota/exception.py

"""
Module: chess.rank.validator.quota.exceptiom
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.system import NullException
from chess.rank import RankException

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


class RankQuotaException(RankException):
    ERROR_CODE = "RANK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Rank.quota raised an exception."


# ======================# NULL RANK_QUOTA EXCEPTIONS #======================#
class NullRankQuotaException(RankQuotaException, NullException):
    ERROR_CODE = "NULL_RANK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Rank.quota cannot be null."


# ======================# RANK_QUOTA BOUNDS EXCEPTIONS #======================#
class RankQuotaBelowBoundsException(RankQuotaException):
    """Raised if the quota zero or less. The lowest quota is 1."""
    ERROR_CODE = "RANK_QUOTA_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Rank.quota cannot be less than one."


class RankQuotaAboveBoundsException(RankQuotaException):
    """Raised if the Rank.ransom is null. This should never happen. It might indicate data inconsistency."""
    ERROR_CODE = "NULL_RANK_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Rank.ransom cannot be null. There may be a data inconsistency or system failure."
    
    
# ======================# RANK_RANSOM INCONSISTENCY EXCEPTIONS #======================#
class KingQuotaException(RankQuotaException):
    """Raised when the ransom assigned to a King differs from the RankSpec value."""
    ERROR_CODE = "_QUEEN_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Queen ransom."


class QueenQuotaException(RankQuotaException):
    """Raised when the ransom assigned to a Queen differs from the RankSpec value."""
    ERROR_CODE = "QUEEN_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Queen quota."


class BishopQuotaException(RankQuotaException):
    """Raised when the ransom assigned to a Bishop differs from the RankSpec value."""
    ERROR_CODE = "BISHOP_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Bishop ransom."


class RookQuotaException(RankQuotaException):
    """Raised when the ransom assigned to a Rook differs from the RankSpec value."""
    ERROR_CODE = "ROOK_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Rook ransom."


class KnightQuotaException(RankQuotaException):
    """Raised when the ransom assigned to a Knight differs from the RankSpec value."""
    ERROR_CODE = "KNIGHT_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Knight ransom."


class PawnQuotaException(RankQuotaException):
    """Raised when the ransom assigned to a Pawn differs from the RankSpec value."""
    ERROR_CODE = "PAWN_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Pawn ransom."