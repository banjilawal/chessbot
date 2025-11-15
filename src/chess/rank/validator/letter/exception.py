# src/chess/rank/validator/letter/exception.py

"""
Module: chess.rank.validator.letter.exceptiom
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
    DEFAULT_MESSAGE = "Rank.letter raised an exception."


# ======================# NULL RANK_LETTER EXCEPTIONS #======================#
class RankLetterNullException(RankLetterException, NullException):
    """Raised if the Rank.letter is null. This should never happen. It might indicate data inconsistency."""
    ERROR_CODE = "NULL_RANK_LETTER_ERROR"
    DEFAULT_MESSAGE = "Rank.letter cannot be null."


# ======================# RANK_LETTER BOUNDS EXCEPTIONS #======================#
class RankLetterOutOfBoundsException(RankLetterException):
    """Raised if the letter is not in RankSpec."""
    ERROR_CODE = "RANK_LETTER_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The letter is not included in the Rank letter specifications."


# ======================# RANK_LETTER INCONSISTENCY EXCEPTIONS #======================#
class KingLetterException(RankLetterException):
    """Raised when the letter assigned to a King differs from the RankSpec value."""
    ERROR_CODE = "_QUEEN_LETTER_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Queen letter."


class QueenLetterException(RankLetterException):
    """Raised when the letter assigned to a Queen differs from the RankSpec value."""
    ERROR_CODE = "QUEEN_LETTER_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Queen letter."


class RookLetterException(RankLetterException):
    """Raised when the letter assigned to a Rook differs from the RankSpec value."""
    ERROR_CODE = "ROOK_LETTER_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Rook letter."
    

class BishopLetterException(RankLetterException):
    """Raised when the letter assigned to a Bishop differs from the RankSpec value."""
    ERROR_CODE = "BISHOP_LETTER_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Bishop letter."


class KnightLetterException(RankLetterException):
    """Raised when the letter assigned to a Knight differs from the RankSpec value."""
    ERROR_CODE = "BISHOP_LETTER_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Bishop letter."


class PawnLetterException(RankLetterException):
    """Raised when the letter assigned to a Pawn differs from the RankSpec value."""
    ERROR_CODE = "ROOK_LETTER_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Rook letter."
    
