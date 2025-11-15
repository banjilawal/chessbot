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

# ======================# TUPLE EXCEPTIONS #======================#
  "NullRankConsistencyTupleException",

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


class RankIdException(RankException):
  ERROR_CODE = "RANK_ID_FIELD_ERROR"
  DEFAULT_MESSAGE = "The visitor_id field of a Rank object raised an exception."

# ======================# NULL RANK_ID EXCEPTIONS #======================#
class RankIdNullException(RankIdException, NullException):
  ERROR_CODE = "RANK_ID_NULL_ERROR"
  DEFAULT_MESSAGE = "Rank.id cannot be null."


# ======================# RANK_ID BOUNDS EXCEPTIONS #======================#
class RankIdAboveBoundsException(RankIdException):
  ERROR_CODE = "RANK_ID_OUT_OF_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "The Rank.id is out of bounds."


# ======================# RANK_ID_INCONSISTENCY EXCEPTIONS #======================#
class RankIdInconsistencyException(RankException):
  ERROR_CODE = "RANK_ID_CONSISTENCY_ERROR"
  DEFAULT_MESSAGE = "Rank and id mismatch."
  

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
