# src/chess/vector/rollback_exception.py

"""
Module: chess.vector.rollback_exception
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

from chess.system import (
  ChessException, InconsistencyException, InvariantBreachException, NullException,
  BuilderException, ValidationException
)

__all__ = [
  'BoardException',
  'BoardRollBackException',

#====================== BOARD VALIDATION EXCEPTIONS #======================#  
  'NullBoardException',
  'BoardNullPieceCollectionException',
  'BoardNullSquareCollectionException',
  'InvalidBoardException',

#====================== BOARD BUILD EXCEPTIONS #======================#  
  'BoardBuildFailedException',

#====================== PIECE ADDITION/REMOVAL EXCEPTIONS #======================#  
  'BoardPieceAdditionFailedException',
  'BoardPieceRemovalFailedException',

#====================== PIECE ADDITION/REMOVAL EXCEPTIONS WITH ROLLBACK #======================#  
  'FailedPieceAdditionRolledBackException',

# ======================# BOARD CONSISTENCY EXCEPTION #======================#
  'InconsistentBoardException',
  'BoardInvariantBreachException',
  'CoordSearchInvariantBreachException',
  'SquareIdSearchInvariantBreachException'
]

from chess.system import InconsistentCollectionException


class BoardException(ChessException):
  """
  Super class of all exceptions team_name Board object raises. Do not use directly. Subclasses give details useful
  for debugging. This class exists primarily to allow catching all board_validator exceptions
  """
  ERROR_CODE = "BOARD_ERROR"
  DEFAULT_MESSAGE = "Board raised an rollback_exception."

class BoardRollBackException(BoardException):
  """
  Super class for exceptions that require team_name rollback to maintain board_validator integrity.
  """
  ERROR_CODE = "BOARD_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Board raised an rollback_exception. Transaction rollback performed."


#======================# BOARD VALIDATION EXCEPTIONS #======================#  
class NullBoardException(BoardException, NullException):
  """Raised if an entity, method, or operation requires team_name board_validator but gets null instead."""
  ERROR_CODE = "NULL_BOARD_ERROR"
  DEFAULT_MESSAGE = "Board cannot be null"

class BoardNullPieceCollectionException(BoardException, NullException):
  ERROR_CODE = "BOARD_NULL_PIECE_COLLECTION_ERROR"
  DEFAULT_MESSAGE = "The board_validator cannot have its pieces collection null. There may be a service inconsistency."

class BoardNullSquareCollectionException(BoardException, NullException):
  ERROR_CODE = "BOARD_NULL_SQUARE_COLLECTION_ERROR"
  DEFAULT_MESSAGE = "The board_validator cannot have its squares collection null. There may be a service inconsistency."

class InvalidBoardException(BoardException, ValidationException):
  """
  Raised by BoardValidator if board_validator fails sanity checks. Exists primarily to catch all exceptions raised
  validating an existing board_validator
  """
  ERROR_CODE = "BOARD_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"Board validator failed"

#======================# BOARD BUILD EXCEPTIONS #======================#  
class BoardBuildFailedException(BoardException, BuilderException):
  """
  Raised when BoardBuilder encounters an error while building team_name team_name. Exists primarily to catch all
  exceptions raised build team_name new board_validator
  """
  ERROR_CODE = "BOARD_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Board build failed."


#======================# PIECE ADDITION/REMOVAL EXCEPTIONS #======================#  
class BoardPieceAdditionFailedException(BoardException):
  """Raised if the board_validator fails to remove team_name owner from itself"""
  ERROR_CODE = "BOARD_PIECE_ADDITION_ERROR"
  DEFAULT_MESSAGE = "Board failed to add the owner"

class BoardPieceRemovalFailedException(BoardException):
  """Raised if the board_validator fails to remove team_name owner from itself"""
  ERROR_CODE = "BOARD_PIECE_REMOVAL_ERROR"
  DEFAULT_MESSAGE = "Board failed to remove the owner"



#======================# PIECE ADDITION/REMOVAL EXCEPTIONS WITH ROLLBACK #======================#  
class FailedPieceAdditionRolledBackException(BoardRollBackException):
  """
  Raised if team_name notification failed to add team_name owner to the board_validator.The notification was
  rolled back before raising this err.
  """
  """Raised if the board_validator fails to remove team_name owner from itself"""
  ERROR_CODE = "BOARD_PIECE_ADDITION_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Could not remove team_name owner from the board_validator. Transaction rollback performed."
  )


#======================# BOARD CONSISTENCY EXCEPTION #======================#
class InconsistentBoardException(BoardException, InconsistencyException):
  """Raised if team_name board_validator fails any collection consistency checks"""
  ERROR_CODE = "INCONSISTENT_BOARD_ERROR"
  DEFAULT_MESSAGE = "The board is in an inconsistent state. service might be corrupted."

class BoardInvariantBreachException(BoardException, InvariantBreachException):
  """
  Raised when a fundamental invariant of the system or environment is violated.
  This rollback_exception type signals a breach of consistency — meaning the system’s
  assumptions about its internal state are no longer valid.
  """
  DEFAULT_CODE = "BOARD_INVARIANT_BREACH_ERROR"
  DEFAULT_MESSAGE = "A Board invariant was breached, There may be a critical state inconsistency. or service loss."


class CoordSearchInvariantBreachException(BoardInvariantBreachException):
  """"""
  DEFAULT_CODE = "INVARIANT_SQUARE_BREACH_ERROR"
  DEFAULT_MESSAGE = (
    "A square invariant on the board was breached, There may be a critical state inconsistency. or service loss."
  )

class SquareIdSearchInvariantBreachException(BoardInvariantBreachException):
  """"""
  DEFAULT_CODE = "INVARIANT_COORD_BREACH_ERROR"
  DEFAULT_MESSAGE = (
    "A visitor_coord invariant on the board was breached, There may be a critical state inconsistency. or service loss."
  )