# src/chess/rank/validator/ransom/exception.py

"""
Module: chess.rank.validator.ransom.exception
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.system import NullException, ValidationException
from chess.rank import RankException


__all__ = [
  "RankRansomException",

# ======================# NULL RANK_RANSOM EXCEPTIONS #======================#
  "NullRankRansomException",
  
# ======================# RANK_RANSOM BOUNDS EXCEPTIONS #======================#
  "RankRansomBelowBoundsException",
  "RankRansomAboveBoundsException",
  
# ======================# RANK_RANSOM INCONSISTENCY EXCEPTIONS #======================#
  "KingRansomException",
  "QueenRansomException",
  "BishopRansomException",
  "RookRansomException",
  "KnightRansomException",
  "PawnRansomException",
]


class RankRansomException(RankException):
  ERROR_CODE = "RANK_RANSOM_FIELD_ERROR"
  DEFAULT_MESSAGE = "Rank.ransom raised an exception."


# ======================# NULL RANK_RANSOM EXCEPTIONS #======================#
class NullRankRansomException(RankRansomException, NullException):
  """Raised if the Rank.ransom is null. This should never happen. It might indicate data inconsistency."""
  ERROR_CODE = "NULL_RANK_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Rank.ransom cannot be null. There may be a data inconsistency or system failure."


# ======================# RANK_RANSOM BOUNDS EXCEPTIONS #======================#
class RankRansomBelowBoundsException(RankRansomException):
  """Raised if the ransom is negative. The lowest ransom is the King's which is zero. """
  ERROR_CODE = "NEGATIVE_RANK_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Rank.ransom cannot be negative. Lowest ransom is zero."


class RankRansomAboveBoundsException(RankRansomException):
  """Raised if the ransom is higher than the Queen's which is 7."""
  ERROR_CODE = "RANK_RANSOM_ABOVE_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "Rank.ransom cannot be higher than the Queen's."


# ======================# RANK_RANSOM_INCONSISTENCY EXCEPTIONS #======================#
class KingRansomException(RankRansomException):
  """Raised when the ransom assigned to a King differs from the RankSpec value."""
  ERROR_CODE = "WRONG_KING_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a King ransom."

class QueenRansomException(RankRansomException):
  """Raised when the ransom assigned to a Queen differs from the RankSpec value."""
  ERROR_CODE = "WRONG_QUEEN_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Queen ransom."

class BishopRansomException(RankRansomException):
  """Raised when the ransom assigned to a Bishop differs from the RankSpec value."""
  ERROR_CODE = "WRONG_BISHOP_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Bishop ransom."

class RookRansomException(RankRansomException):
  """Raised when the ransom assigned to a Rook differs from the RankSpec value."""
  ERROR_CODE = "WRONG_ROOK_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Rook ransom."

class KnightRansomException(RankRansomException):
  """Raised when the ransom assigned to a Knight differs from the RankSpec value."""
  ERROR_CODE = "WRONG_KNIGHT_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Knight ransom."

class PawnRansomException(RankRansomException):
  """Raised when the ransom assigned to a Pawn differs from the RankSpec value."""
  ERROR_CODE = "WRONG_PAWN_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Pawn ransom."