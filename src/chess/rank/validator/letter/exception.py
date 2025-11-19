# src/chess/rank/coord_stack_validator/designation/exception.py

"""
Module: chess.rank.coord_stack_validator.designation.exceptiom
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.system import NullException
from chess.rank import RankException

__all__ = [
    "RankLetterException",
    
    # ======================# NULL RANK_LETTER EXCEPTIONS #======================#
    "RankLetterNullException",
    
    # ======================# RANK_LETTER BOUNDS EXCEPTIONS #======================#
    "RankLetterOutOfBoundsException",
    
    # ======================# RANK_LETTER_INCONSISTENCY EXCEPTIONS #======================#
    "KingLetterException",
    "QueenLetterException",
    "BishopLetterException",
    "RookLetterException",
    "KnightLetterException",
    "PawnLetterException",
]


class RankLetterException(RankException):
    """
    Super class of exceptions raised by Letter objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_LETTER_ERROR"
    DEFAULT_MESSAGE = "Rank.designation raised an exception."


# ======================# NULL RANK_LETTER EXCEPTIONS #======================#
class RankLetterNullException(RankLetterException, NullException):
    """Raised if the Rank.designation is null. This should never happen. It might indicate data inconsistency."""
    ERROR_CODE = "NULL_RANK_LETTER_ERROR"
    DEFAULT_MESSAGE = "Rank.designation cannot be null."


# ======================# RANK_LETTER BOUNDS EXCEPTIONS #======================#
class RankLetterOutOfBoundsException(RankLetterException):
    """Raised if the designation is not in RankSpec."""
    ERROR_CODE = "RANK_LETTER_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The designation is not included in the Rank designation specifications."


# ======================# RANK_LETTER INCONSISTENCY EXCEPTIONS #======================#
class KingLetterException(RankLetterException):
    """Raised when the designation assigned to a King differs from the RankSpec value."""
    ERROR_CODE = "_QUEEN_LETTER_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Queen designation."


class QueenLetterException(RankLetterException):
    """Raised when the designation assigned to a Queen differs from the RankSpec value."""
    ERROR_CODE = "QUEEN_LETTER_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Queen designation."


class RookLetterException(RankLetterException):
    """Raised when the designation assigned to a Rook differs from the RankSpec value."""
    ERROR_CODE = "ROOK_LETTER_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Rook designation."
    

class BishopLetterException(RankLetterException):
    """Raised when the designation assigned to a Bishop differs from the RankSpec value."""
    ERROR_CODE = "BISHOP_LETTER_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Bishop designation."


class KnightLetterException(RankLetterException):
    """Raised when the designation assigned to a Knight differs from the RankSpec value."""
    ERROR_CODE = "BISHOP_LETTER_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Bishop designation."


class PawnLetterException(RankLetterException):
    """Raised when the designation assigned to a Pawn differs from the RankSpec value."""
    ERROR_CODE = "ROOK_LETTER_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Rook designation."
    
