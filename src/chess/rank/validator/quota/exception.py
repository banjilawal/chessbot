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
    "RankQuotaException",
    
    # ======================# NULL RANK_QUOTA EXCEPTIONS #======================#
    "NullRankQuotaException",
    
    # ======================# RANK_QUOTA BOUNDS EXCEPTIONS #======================#
    "RankQuotaBelowBoundsException",
    "RankQuotaAboveBoundsException",
    
    # ======================# RANK_QUOTA_INCONSISTENCY EXCEPTIONS #======================#
    "RankQuotaInconsistencyException",
    
    # ======================# RANK_QUOTA_INCONSISTENCY EXCEPTIONS #======================#
    "WrongKingQuotaException",
    "WrongQueenQuotaException",
    "WrongBishopQuotaException",
    "WrongRookQuotaException",
    "WrongKnightQuotaException",
    "WrongPawnQuotaException",
]


class RankQuotaException(RankException):
    ERROR_CODE = "RANK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Rank.quota raised an exception."


# ======================# NULL RANK_QUOTA EXCEPTIONS #======================#
class NullRankQuotaException(RankQuotaException, NullException):
    ERROR_CODE = "NULL_RANK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Rank.quota cannot be null."


# ======================# RANK_QUOTA BOUNDS EXCEPTIONS #======================#
class RankQuotaBelowBoundsException(RankQuotaException):
    ERROR_CODE = "RANK_QUOTA_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "A Rank instance cannot have a quota below one."


class RankQuotaAboveBoundsException(RankQuotaException):
    ERROR_CODE = "RANK_QUOTA_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The Pawn has the highest quota. The value is above quota bounds."


# ======================# RANK_QUOTA_INCONSISTENCY EXCEPTIONS #======================#
class RankQuotaInconsistencyException(RankException):
    ERROR_CODE = "RANK_QUOTA_CONSISTENCY_ERROR"
    DEFAULT_MESSAGE = "Rank and quota do not match."


class WrongKingQuotaException(RankQuotaException):
    ERROR_CODE = "WRONG_KING_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a King quota."


class WrongQueenQuotaException(RankQuotaException):
    ERROR_CODE = "WRONG_QUEEN_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Queen quota."


class WrongBishopQuotaException(RankQuotaException):
    ERROR_CODE = "WRONG_BISHOP_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Bishop quota."


class WrongRookQuotaException(RankQuotaException):
    ERROR_CODE = "WRONG_ROOK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Rook quota."


class WrongKnightQuotaException(RankQuotaException):
    ERROR_CODE = "WRONG_BISHOP_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Bishop quota."


class WrongPawnQuotaException(RankQuotaException):
    ERROR_CODE = "WRONG_ROOK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Incorrect value for a Rook quota."
