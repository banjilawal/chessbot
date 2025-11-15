# src/chess/bounds/validator/exception.py

"""
Module: chess.bounds.validator.exception
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, validator, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each consistency and behavior in the `Vector` class has an rollback_exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` graph.
2. Fast debugging using highly granular rollback_exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` graph.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
"""

from chess.system import NullException, ValidationException
from chess.rank import (
    RankException, RankRansomException, RankQuotaException, RankNameException, RankLetterException, RankIdException
)

__all__ = [
    "RankLetterException",
    
# ======================# NULL RANK_LETTER EXCEPTIONS #======================#
    "NullRankLetterException",
    
# ======================# RANK_LETTER BOUNDS EXCEPTIONS #======================#
    "RankLetterOutOfBoundsException",
    
 # ======================# RANK_LETTER_INCONSISTENCY EXCEPTIONS #======================#
    "RankLetterInconsistencyException",
    "WrongKingLetterException",
    "WrongQueenLetterException",
    "WrongBishopLetterException",
    "WrongRookLetterException",
    "WrongKnightLetterException",
    "WrongPawnLetterException",
]


class RankLetterException(RankException):
    ERROR_CODE = "RANK_LETTER_FIELD_ERROR"
    DEFAULT_MESSAGE = "The letter field of a Rank object raised an exception."


# ======================# NULL RANK_LETTER EXCEPTIONS #======================#
class NullRankLetterException(RankLetterException, NullException):
    ERROR_CODE = "NULL_RANK_LETTER_ERROR"
    DEFAULT_MESSAGE = "A Rank object cannot have a null letter field."


# ======================# RANK_LETTER BOUNDS EXCEPTIONS #======================#
class RankLetterOutOfBoundsException(RankLetterException):
    ERROR_CODE = "RANK_LETTER_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The letter is not included in the Rank letter specifications."


# ======================# RANK_LETTER_INCONSISTENCY EXCEPTIONS #======================#
class RankLetterInconsistencyException(RankException):
    ERROR_CODE = "RANK_LETTER_CONSISTENCY_ERROR"
    DEFAULT_MESSAGE = "Rank and letter mismatch."


class WrongKingLetterException(RankLetterException):
    ERROR_CODE = "WRONG_KING_LETTER_ERROR"
    DEFAULT_MESSAGE = f"Incorrect value for a King letter."


class WrongQueenLetterException(RankLetterException):
    ERROR_CODE = "WRONG_QUEEN_LETTER_ERROR"
    DEFAULT_MESSAGE = f"Incorrect value for a Queen letter."


class WrongRookLetterException(RankLetterException):
    ERROR_CODE = "WRONG_ROOK_LETTER_ERROR"
    DEFAULT_MESSAGE = f"Incorrect value for a Rook letter."


class WrongBishopLetterException(RankLetterException):
    ERROR_CODE = "WRONG_BISHOP_LETTER_ERROR"
    DEFAULT_MESSAGE = f"Incorrect value for a Bishop letter."


class WrongKnightLetterException(RankLetterException):
    ERROR_CODE = "WRONG_BISHOP_LETTER_ERROR"
    DEFAULT_MESSAGE = f"Incorrect value for a Bishop letter."


class WrongPawnLetterException(RankLetterException):
    ERROR_CODE = "WRONG_ROOK_LETTER_ERROR"
    DEFAULT_MESSAGE = f"Incorrect value for a Rook letter."
