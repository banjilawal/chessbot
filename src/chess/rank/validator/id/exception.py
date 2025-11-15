# src/chess/rank/validator/id/exception.py

"""
Module: chess.rank.validator.id.exceptiom
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.system import NullException
from chess.rank import RankException

__all__ = [
    "RankIdException",
    
    # ======================# NULL RANK_ID EXCEPTIONS #======================#
  "RankIdNullException",
    
    # ======================# RANK_ID BOUNDS EXCEPTIONS #======================#
    "RankIdAboveBoundsException",
    
    # ======================# RANK_ID_INCONSISTENCY EXCEPTIONS #======================#
    "KingIdException",
    "QueenIdException",
    "BishopIdException",
    "RookIdException",
    "KnightIdException",
    "PawnIdException",
]


class RankIdException(RankException):
    """
  Super class of exceptions raised by Id objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
    ERROR_CODE = "RANK_ID_ERROR"
    DEFAULT_MESSAGE = "Rank.id raised an exception."


# ======================# NULL RANK_ID EXCEPTIONS #======================#
class RankIdNullException(RankIdException, NullException):
    """Raised if the Rank.id is null. This should never happen. It might indicate data inconsistency."""
    ERROR_CODE = "NULL_RANK_ID_ERROR"
    DEFAULT_MESSAGE = "Rank.id cannot be null."


# ======================# RANK_ID BOUNDS EXCEPTIONS #======================#
class RankIdAboveBoundsException(RankIdException):
    """Raise if the id exceecs RankSoec,max_id"""
    ERROR_CODE = "NULL_RANK_ID_ERROR"
    DEFAULT_MESSAGE = "Rank.id larger than RankSpec.max_id."


# ======================# RANK_ID INCONSISTENCY EXCEPTIONS #======================#
class KingIdException(RankIdException):
    """Raised when the id assigned to a King differs from the RankSpec value."""
    ERROR_CODE = "KING_ID_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a King id."


class QueenIdException(RankIdException):
    """Raised when the id assigned to a Queen differs from the RankSpec value."""
    ERROR_CODE = "QUEEN_ID_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Queen id."


class BishopIdException(RankIdException):
    """Raised when the id assigned to a Bishop differs from the RankSpec value."""
    ERROR_CODE = "BISHOP_ID_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Bishop id."


class RookIdException(RankIdException):
    """Raised when the id assigned to a Rook differs from the RankSpec value."""
    ERROR_CODE = "ROOK_ID_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Rook id."


class KnightIdException(RankIdException):
    """Raised when the id assigned to a Knight differs from the RankSpec value."""
    ERROR_CODE = "BISHOP_ID_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Bishop id."


class PawnIdException(RankIdException):
    """Raised when the id assigned to a Pawn differs from the RankSpec value."""
    ERROR_CODE = "ROOK_ID_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Rook id."