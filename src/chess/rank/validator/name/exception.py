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

from chess.system import NullException
from chess.rank import RankException

__all__ = [
  "RankNameException",

# ======================# NULL RANK_NAME EXCEPTIONS #======================#
  "RankNameNullException",

# ======================# RANK_NAME BOUNDS EXCEPTIONS #======================#
  "RankNameOutOfBoundsException",

# ======================# RANK_NAME INCONSISTENCY EXCEPTIONS #======================#
  "RankNameInconsistencyException",
  
  # ======================# RANK_NAME_INCONSISTENCY EXCEPTIONS #======================#
  "WrongKingNameException",
  "WrongQueenNameException",
  "WrongBishopNameException",
  "WrongRookNameException",
  "WrongKnightNameException",
  "WrongPawnNameException",
]


class RankNameException(RankException):
  ERROR_CODE = "RANK_NAME_ERROR"
  DEFAULT_MESSAGE = "Rank.name raised an exception."


# ======================# NULL RANK_NAME EXCEPTIONS #======================#
class RankNameNullException(RankException, NullException):
  ERROR_CODE = "RANK_NAME_NULL_ERROR"
  DEFAULT_MESSAGE = "Rank.name cannot be null."


# ======================# RANK_NAME BOUNDS EXCEPTIONS #======================#
class RankNameOutOfBoundsException(RankNameException):
  ERROR_CODE = "RANK_NAME_OUT_OF_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "The name is not included in the Rank name specifications."


# ======================# RANK_NAME INCONSISTENCY EXCEPTIONS #======================#
class RankNameInconsistencyException(RankException):
  ERROR_CODE = "RANK_NAME_CONSISTENCY_ERROR"
  DEFAULT_MESSAGE = "Rank and name don't match."
  

class WrongKingNameException(RankNameException):
  ERROR_CODE = "WRONG_KING_NAME_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a King name."


class WrongQueenNameException(RankNameException):
  ERROR_CODE = "WRONG_QUEEN_NAME_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Queen name."


class WrongRookNameException(RankNameException):
  ERROR_CODE = "WRONG_ROOK_NAME_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Rook name."

class WrongBishopNameException(RankNameException):
  ERROR_CODE = "WRONG_BISHOP_NAME_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Bishop name."

class WrongKnightNameException(RankNameException):
  ERROR_CODE = "WRONG_RANK_NAME_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Knight name."


class WrongPawnNameException(RankNameException):
  ERROR_CODE = "WRONG_PAWN_NAME_ERROR"
  DEFAULT_MESSAGE = "Incorrect value for a Pawn name."