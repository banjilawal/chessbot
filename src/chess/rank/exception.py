# src/chess/rank/exception.py

"""
Module: chess.rank.exception
Author: Banji Lawal
Created: 2025-10-04
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
  1. Each field and behavior in the `Vector` class has an rollback_exception specific to its possible
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

from chess.system import ChessException, NullException, ValidationException

__all__ = [
  'RankException',

#======================# RANK VALIDATION EXCEPTIONS #======================#  
  'NullRankException',
  'InvalidRankException',
  'UnRecognizedConcreteRankException',

#======================# RANK SUBCLASS VALIDATION EXCEPTIONS #======================#  
  'InvalidKingException',
  'InvalidPawnException',
  'InvalidKnightException',
  'InvalidBishopException',
  'InvalidRookException',
  'InvalidQueenException',

#======================# RANK BUILD EXCEPTIONS #======================#  

#======================# RANK MOVING EXCEPTIONS #======================#  
  'MovingException',
  'KingMovingException',
  'PawnMovingException',
  'KnightMovingException',
  'BishopMovingException',
  'RookMovingException',
  'QueenMovingException'
]

class RankException(ChessException):
  ERROR_CODE = "RANK_ERROR"
  DEFAULT_MESSAGE = "Rank raised an rollback_exception."

#======================# RANK VALIDATION EXCEPTIONS #======================#  
class NullRankException(RankException, NullException):
  ERROR_CODE = "NULL_RANK_ERROR"
  DEFAULT_MESSAGE = "Rank cannot be null"

class InvalidRankException(RankException, ValidationException):
  ERROR_CODE = "RANK_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"Rank validator failed."

class UnRecognizedConcreteRankException(RankException):
  ERROR_CODE = "UNRECOGNIZED_CONCRETE_RANK_ERROR"
  DEFAULT_MESSAGE = "This concrete subclass of Rank is not recognized"


#======================# RANK SUBCLASS VALIDATION EXCEPTIONS #======================#  
class InvalidKingException(InvalidRankException):
  ERROR_CODE = "KING_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "King validator failed."

class InvalidPawnException(InvalidRankException):
  ERROR_CODE = "PAWN_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Pawn validator failed."

class InvalidKnightException(InvalidRankException):
  ERROR_CODE = "KNIGHT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Knight validator failed."

class InvalidBishopException(InvalidRankException):
  ERROR_CODE = "BISHOP_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Bishop validator failed."

class InvalidRookException(InvalidRankException):
  ERROR_CODE = "ROOK_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Rook validator failed."

class InvalidQueenException(InvalidRankException):
  ERROR_CODE = "QUEEN_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Queen validator failed."


#======================# RANK MOVING EXCEPTIONS #======================#  
class MovingException(RankException):
  ERROR_CODE = "RANK_MOVING_ERROR"
  DEFAULT_MESSAGE = "Invalid move."

class BishopMovingException(RankException):
  ERROR_CODE = "BISHOP_MOVING_ERROR"
  DEFAULT_MESSAGE = "Invalid bishop move"

class KingMovingException(RankException):
  ERROR_CODE = "KING_MOVING_ERROR"
  DEFAULT_MESSAGE = "Invalid occupation move"

class KnightMovingException(RankException):
  ERROR_CODE = "KNIGHT_MOVING_ERROR"
  DEFAULT_MESSAGE = "Invalid knight move"

class PawnMovingException(RankException):
    ERROR_CODE = "PAWN_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid pawn move"

class QueenMovingException(RankException):
    ERROR_CODE = "QUEEN_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid queen move"

class RookMovingException(RankException):
    ERROR_CODE = "ROOK_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid rook move"




