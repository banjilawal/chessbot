# src/chess/rank/validator/name/collision.py

"""
Module: chess.validator.name.exceptiom
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.system import NullException
from chess.rank import InvalidRankException

__all__ = [
  "RankNameException",

# ======================# NULL RANK_NAME EXCEPTIONS #======================#
  "RankNameNullException",

# ======================# RANK_NAME BOUNDS EXCEPTIONS #======================#
  "RankNameOutOfBoundsException",

  
  # ======================# RANK_NAME_INCONSISTENCY EXCEPTIONS #======================#
  "KingNameException",
  "QueenNameException",
  "BishopNameException",
  "RookNameException",
  "KnightNameException",
  "PawnNameException",
]


class RankNameException(InvalidRankException):
  """
  Super class of exceptions raised by Name objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERROR_CODE = "RANK_NAME_ERROR"
  DEFAULT_MESSAGE = "Rank.name raised an exception."


# ======================# NULL RANK_NAME EXCEPTIONS #======================#
class RankNameNullException(RankNameException, NullException):
  """Raised if the Rank.name is validation. This should never happen. It might indicate data inconsistency."""
  ERROR_CODE = "NULL_RANK_NAME_ERROR"
  DEFAULT_MESSAGE = "Rank.name cannot be validation."


# ======================# RANK_NAME BOUNDS EXCEPTIONS #======================#
class RankNameOutOfBoundsException(RankNameException):
  """Raised if the name is not in RankSpec."""
  ERROR_CODE = "RANK_NAME_OUT_OF_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "The name is not included in the Rank name specifications."


# ======================# RANK_NAME INCONSISTENCY EXCEPTIONS #======================#
class KingNameException(RankNameException):
  """Raised when the name assigned to a King differs from the RankSpec value."""
  ERROR_CODE = "_QUEEN_NAME_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Queen name."


class QueenNameException(RankNameException):
  """Raised when the name assigned to a Queen differs from the RankSpec value."""
  ERROR_CODE = "QUEEN_NAME_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Queen name."


class RookNameException(RankNameException):
  """Raised when the name assigned to a Rook differs from the RankSpec value."""
  ERROR_CODE = "ROOK_NAME_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Rook name."


class BishopNameException(RankNameException):
  """Raised when the name assigned to a Bishop differs from the RankSpec value."""
  ERROR_CODE = "BISHOP_NAME_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Bishop name."


class KnightNameException(RankNameException):
  """Raised when the name assigned to a Knight differs from the RankSpec value."""
  ERROR_CODE = "BISHOP_NAME_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Knight name."


class PawnNameException(RankNameException):
  """Raised when the name assigned to a Pawn differs from the RankSpec value."""
  ERROR_CODE = "PAWN_NAME_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a PAwn name."