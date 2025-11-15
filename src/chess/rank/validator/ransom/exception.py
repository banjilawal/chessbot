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
from chess.rank import RankException


__all__ = [
  "RankRansomException",

# ======================# NULL RANK_RANSOM EXCEPTIONS #======================#
  "NullRankRansomException",
  
# ======================# RANK_RANSOM BOUNDS EXCEPTIONS #======================#
  "RankRansomBelowBoundsException",
  "RankRansomAboveBoundsException",
  
# ======================# RANK_RANSOM INCONSISTENCY EXCEPTIONS #======================#
  "WrongKingRansomException",
  "WrongQueenRansomException",
  "WrongBishopRansomException",
  "WrongRookRansomException",
  "WrongKnightRansomException",
  "WrongPawnRansomException",
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


# ======================# RANK_CONSISTENCY EXCEPTIONS #======================#
class RankRansomInconsistencyException(RankException):
  ERROR_CODE = "RANK_RANSOM_CONSISTENCY_ERROR"
  DEFAULT_MESSAGE = "The rank and ransom do not match."
  

# ======================# RANK_RANSOM_INCONSISTENCY EXCEPTIONS #======================#
class WrongKingRansomException(RankRansomException):
  ERROR_CODE = "WRONG_KING_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a King ransom."

class WrongQueenRansomException(RankRansomException):
  ERROR_CODE = "WRONG_QUEEN_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Queen ransom."

class WrongBishopRansomException(RankRansomException):
  ERROR_CODE = "WRONG_BISHOP_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Bishop ransom."

class WrongRookRansomException(RankRansomException):
  ERROR_CODE = "WRONG_ROOK_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Rook ransom."

class WrongKnightRansomException(RankRansomException):
  ERROR_CODE = "WRONG_KNIGHT_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Knight ransom."

class WrongPawnRansomException(RankRansomException):
  ERROR_CODE = "WRONG_PAWN_RANSOM_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Pawn ransom."
