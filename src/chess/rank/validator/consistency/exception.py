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
  RankRansomException, RankQuotaException, RankNameException, RankLetterException, RankIdException
)

__all__ = [

# ======================# RANK_RANSOM_INCONSISTENCY EXCEPTIONS #======================#
  "WrongKingRansomException",
  "WrongQueenRansomException",
  "WrongBishopRansomException",
  "WrongRookRansomException",
  "WrongKnightRansomException",
  "WrongPawnRansomException",
  
  # ======================# RANK_QUOTA_INCONSISTENCY EXCEPTIONS #======================#
  "WrongKingQuotaException",
  "WrongQueenQuotaException",
  "WrongBishopQuotaException",
  "WrongRookQuotaException",
  "WrongKnightQuotaException",
  "WrongPawnQuotaException",
  
  # ======================# RANK_NAME_INCONSISTENCY EXCEPTIONS #======================#
  "WrongKingNameException",
  "WrongQueenNameException",
  "WrongBishopNameException",
  "WrongRookNameException",
  "WrongKnightNameException",
  "WrongPawnNameException",
  
  # ======================# RANK_LETTER_INCONSISTENCY EXCEPTIONS #======================#
  "WrongKingLetterException",
  "WrongQueenLetterException",
  "WrongBishopLetterException",
  "WrongRookLetterException",
  "WrongKnightLetterException",
  "WrongPawnLetterException",
  
  # ======================# RANK_ID_INCONSISTENCY EXCEPTIONS #======================#
  "WrongKingIdException",
  "WrongQueenIdException",
  "WrongBishopIdException",
  "WrongRookIdException",
  "WrongKnightIdException",
  "WrongPawnIdException"
]


# ======================# RANK_RANSOM_INCONSISTENCY EXCEPTIONS #======================#
class WrongKingRansomException(RankRansomException):
  ERROR_CODE = "WRONG_KING_RANSOM_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a King ransom."

class WrongQueenRansomException(RankRansomException):
  ERROR_CODE = "WRONG_QUEEN_RANSOM_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Queen ransom."

class WrongBishopRansomException(RankRansomException):
  ERROR_CODE = "WRONG_BISHOP_RANSOM_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Bishop ransom."

class WrongRookRansomException(RankRansomException):
  ERROR_CODE = "WRONG_ROOK_RANSOM_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Rook ransom."

class WrongKnightRansomException(RankRansomException):
  ERROR_CODE = "WRONG_RANK_RANSOM_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Knight ransom."

class WrongPawnRansomException(RankRansomException):
  ERROR_CODE = "WRONG_PAWN_RANSOM_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Pawn ransom."


# ======================# RANK_QUOTA_INCONSISTENCY EXCEPTIONS #======================#
class WrongKingQuotaException(RankQuotaException):
  ERROR_CODE = "WRONG_KING_QUOTA_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a King quota."


class WrongQueenQuotaException(RankQuotaException):
  ERROR_CODE = "WRONG_QUEEN_QUOTA_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Queen quota."


class WrongBishopQuotaException(RankQuotaException):
  ERROR_CODE = "WRONG_BISHOP_QUOTA_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Bishop quota."


class WrongRookQuotaException(RankQuotaException):
  ERROR_CODE = "WRONG_ROOK_QUOTA_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Rook quota."


class WrongKnightQuotaException(RankQuotaException):
  ERROR_CODE = "WRONG_BISHOP_QUOTA_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Bishop quota."


class WrongPawnQuotaException(RankQuotaException):
  ERROR_CODE = "WRONG_ROOK_QUOTA_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Rook quota."


class WrongKnightQuotaException(RankQuotaException):
  ERROR_CODE = "WRONG_RANK_QUOTA_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Knight quota."


class WrongPawnQuotaException(RankQuotaException):
  ERROR_CODE = "WRONG_PAWN_QUOTA_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Pawn quota."


# ======================# RANK_NAME_INCONSISTENCY EXCEPTIONS #======================#
class WrongKingNameException(RankNameException):
  ERROR_CODE = "WRONG_KING_NAME_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a King name."


class WrongQueenNameException(RankNameException):
  ERROR_CODE = "WRONG_QUEEN_NAME_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Queen name."


class WrongRookNameException(RankNameException):
  ERROR_CODE = "WRONG_ROOK_NAME_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Rook name."

class WrongBishopNameException(RankNameException):
  ERROR_CODE = "WRONG_BISHOP_NAME_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Bishop name."

class WrongKnightNameException(RankNameException):
  ERROR_CODE = "WRONG_RANK_NAME_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Knight name."


class WrongPawnNameException(RankNameException):
  ERROR_CODE = "WRONG_PAWN_NAME_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Pawn name."


# ======================# RANK_LETTER_INCONSISTENCY EXCEPTIONS #======================#
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



# ======================# RANK_ID_INCONSISTENCY EXCEPTIONS #======================#
class WrongKingIdException(RankIdException):
  ERROR_CODE = "WRONG_KING_ID_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a King id."


class WrongQueenIdException(RankIdException):
  ERROR_CODE = "WRONG_QUEEN_ID_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Queen id."


class WrongRookIdException(RankIdException):
  ERROR_CODE = "WRONG_ROOK_ID_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Rook id."

class WrongBishopIdException(RankIdException):
  ERROR_CODE = "WRONG_BISHOP_ID_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Bishop id."
  

class WrongKnightIdException(RankIdException):
  ERROR_CODE = "WRONG_BISHOP_ID_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Bishop id."


class WrongPawnIdException(RankIdException):
  ERROR_CODE = "WRONG_ROOK_ID_ERROR"
  DEFAULT_MESSAGE = f"Incorrect value for a Rook id."
