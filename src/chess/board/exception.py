# src/chess/vector/exception.py

"""
Module: chess.vector.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each field and behavior in the `Vector` class has an exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` domain.
2. Fast debugging using highly granular exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` domain.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
"""

from chess.system import ChessException, NullException, BuilderException, ValidationException

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
  'FailedPieceRemovalRolledBackException',
]

from chess.system import InconsistentCollectionException


class BoardException(ChessException):
  """
  Super class of all exceptions team Board object raises. Do not use directly. Subclasses give details useful
  for debugging. This class exists primarily to allow catching all board exceptions
  """
  ERROR_CODE = "BOARD_ERROR"
  DEFAULT_MESSAGE = "Board raised an exception."

class BoardRollBackException(BoardException):
  """
  Super class for exceptions that require team rollback to maintain board integrity.
  """
  ERROR_CODE = "BOARD_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Board raised an exception. Transaction rollback performed."


#======================# BOARD VALIDATION EXCEPTIONS #======================#  
class NullBoardException(BoardException, NullException):
  """Raised if an entity, method, or operation requires team board but gets null instead."""
  ERROR_CODE = "NULL_BOARD_ERROR"
  DEFAULT_MESSAGE = "Board cannot be null"

class BoardNullPieceCollectionException(BoardException, NullException):
  ERROR_CODE = "BOARD_NULL_PIECE_COLLECTION_ERROR"
  DEFAULT_MESSAGE = "The board cannot have its pieces collection null. There may be a data inconsistency."

class BoardNullSquareCollectionException(BoardException, NullException):
  ERROR_CODE = "BOARD_NULL_SQUARE_COLLECTION_ERROR"
  DEFAULT_MESSAGE = "The board cannot have its squares collection null. There may be a data inconsistency."

class InvalidBoardException(BoardException, ValidationException):
  """
  Raised by BoardValidator if board fails sanity checks. Exists primarily to catch all exceptions raised
  validating an existing board
  """
  ERROR_CODE = "BOARD_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"Board validation failed"

#======================# BOARD BUILD EXCEPTIONS #======================#  
class BoardBuildFailedException(BoardException, BuilderException):
  """
  Raised when BoardBuilder encounters an error while building team team. Exists primarily to catch all
  exceptions raised build team new board
  """
  ERROR_CODE = "BOARD_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Board build failed."


#======================# PIECE ADDITION/REMOVAL EXCEPTIONS #======================#  
class BoardPieceAdditionFailedException(BoardException):
  """Raised if the board fails to remove team piece from itself"""
  ERROR_CODE = "BOARD_PIECE_ADDITION_ERROR"
  DEFAULT_MESSAGE = "Board failed to add the piece"

class BoardPieceRemovalFailedException(BoardException):
  """Raised if the board fails to remove team piece from itself"""
  ERROR_CODE = "BOARD_PIECE_REMOVAL_ERROR"
  DEFAULT_MESSAGE = "Board failed to remove the piece"



#======================# PIECE ADDITION/REMOVAL EXCEPTIONS WITH ROLLBACK #======================#  
class FailedPieceAdditionRolledBackException(BoardRollBackException):
  """
  Raised if team transaction failed to add team piece to the board.The transaction was
  rolled back before raising this err.
  """
  """Raised if the board fails to remove team piece from itself"""
  ERROR_CODE = "BOARD_PIECE_ADDITION_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Could not remove team piece from the board. Transaction rollback performed."
  )

class FailedPieceRemovalRolledBackException(BoardRollBackException):
  """
  Raised if team transaction failed to remove team piece from the board's list of pieces.
  The transaction was rolled back before raising this err.
  """
  ERROR_CODE = "BOARD_PIECE_REMOVAL_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Could not remove team piece from the board. Transaction rollback performed."
  )

class InconsistentBoardException(BoardException, InconsistentCollectionException):
  """Raised if team board fails any collection consistency checks"""
  ERROR_CODE = "INCONSISTENT_BOARD_ERROR"
  DEFAULT_MESSAGE = "The board is an inconsistent state. data might be corrupted."