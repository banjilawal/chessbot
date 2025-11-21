# src/chess/rank/validator/designation/collision.py

"""
Module: chess.rank.validator.designation.exceptiom
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.system import NullException
from chess.rank import InvalidRankException, RankException

__all__ = [
    "RankDesignationException",
    
    # ======================# NULL RANK_DESIGNATION EXCEPTIONS #======================#
    "NullRankDesignationException",
    
    # ======================# RANK_DESIGNATION BOUNDS EXCEPTIONS #======================#
    "RankDesignationBoundsException",
    
    # ======================# RANK_DESIGNATION_INCONSISTENCY EXCEPTIONS #======================#
    "KingDesignationException",
    "QueenDesignationException",
    "BishopDesignationException",
    "RookDesignationException",
    "KnightDesignationException",
    "PawnDesignationException",
]


class RankDesignationException(InvalidRankException):
    """
    Super class of exceptions raised by Designation objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Rank.designation raised an exception."


# ======================# NULL RANK_DESIGNATION EXCEPTIONS #======================#
class NullRankDesignationException(RankDesignationException, NullException):
    """Raised if the Rank.designation is validation. This should never happen. It might indicate data inconsistency."""
    ERROR_CODE = "NULL_RANK_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Rank.designation cannot be validation."


# ======================# RANK_DESIGNATION BOUNDS EXCEPTIONS #======================#
class RankDesignationBoundsException(RankDesignationException):
    """Raised if the designation is not in RankSpec."""
    ERROR_CODE = "RANK_DESIGNATION_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The designation is not included in the Rank designation specifications."


# ======================# RANK_DESIGNATION INCONSISTENCY EXCEPTIONS #======================#
class KingDesignationException(RankDesignationException):
    """Raised when the designation assigned to a King differs from the RankSpec value."""
    ERROR_CODE = "_QUEEN_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Queen designation."


class QueenDesignationException(RankDesignationException):
    """Raised when the designation assigned to a Queen differs from the RankSpec value."""
    ERROR_CODE = "QUEEN_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Queen designation."


class RookDesignationException(RankDesignationException):
    """Raised when the designation assigned to a Rook differs from the RankSpec value."""
    ERROR_CODE = "ROOK_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Rook designation."
    

class BishopDesignationException(RankDesignationException):
    """Raised when the designation assigned to a Bishop differs from the RankSpec value."""
    ERROR_CODE = "BISHOP_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Bishop designation."


class KnightDesignationException(RankDesignationException):
    """Raised when the designation assigned to a Knight differs from the RankSpec value."""
    ERROR_CODE = "BISHOP_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Bishop designation."


class PawnDesignationException(RankDesignationException):
    """Raised when the designation assigned to a Pawn differs from the RankSpec value."""
    ERROR_CODE = "ROOK_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Rook designation."
    
