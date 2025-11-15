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
  ERROR_CODE = "NULL_RANK_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Rank.ransom cannot be null."


# ======================# RANK_RANSOM BOUNDS EXCEPTIONS #======================#
class RankRansomBelowBoundsException(RankRansomException):
  ERROR_CODE = "NEGATIVE_RANK_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Rank.ransom cannot be negative."


class RankRansomAboveBoundsException(RankRansomException):
  ERROR_CODE = "RANK_RANSOM_ABOVE_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "Rank.ransom cannot be higher than the Queen's."


# ======================# RANK_RANSOM_INCONSISTENCY EXCEPTIONS #======================#
class KingRansomException(RankRansomException):
  ERROR_CODE = "WRONG_KING_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a King ransom."

class QueenRansomException(RankRansomException):
  ERROR_CODE = "WRONG_QUEEN_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Queen ransom."

class BishopRansomException(RankRansomException):
  ERROR_CODE = "WRONG_BISHOP_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Bishop ransom."

class RookRansomException(RankRansomException):
  ERROR_CODE = "WRONG_ROOK_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Rook ransom."

class KnightRansomException(RankRansomException):
  ERROR_CODE = "WRONG_KNIGHT_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Knight ransom."

class PawnRansomException(RankRansomException):
  ERROR_CODE = "WRONG_PAWN_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Pawn ransom."
