# src/chess/board/exception.py

"""
Module: chess.board.exception
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
    ChessException, BuildFailedException, InvariantBreachException, NullException, RollbackException,
    ValidationException
)

__all__ = [
    "BoardException",
    
#====================== BOARD VALIDATION EXCEPTIONS #======================#
    "NullBoardException",
    "BoardNullPieceListException",
    "BoardNullSquareListException",
    "NumberOfBoardSquaresOutOfBoundsException",
    "InvalidBoardException",
    
#====================== BOARD BUILD EXCEPTIONS #======================#
    "BoardBuildFailedException",
    
#====================== PIECE ADDITION/REMOVAL EXCEPTIONS WITH ROLLBACK #======================#
    "FailedPieceAdditionRolledBackException",
    "FailedPieceRemovalRolledBackException",
    
#======================# BOARD CONSISTENCY EXCEPTION #======================#
    "CoordSearchInvariantBreachException",
    "SquareInvariantBreachException"
]




class BoardException(ChessException):
    """
    Super class of exceptions raised by a Board object. Do not use directly. Subclasses give
    targeted, fined grained, debugging info.
    """
    ERROR_CODE = "BOARD_ERROR"
    DEFAULT_MESSAGE = "Board raised an rollback_exception."


# ======================# NULL DOMAIN EXCEPTIONS #======================#
class NullBoardException(BoardException, NullException):
    """Raised if an entity, method, or operation requires Board but gets null instead."""
    ERROR_CODE = "NULL_BOARD_ERROR"
    DEFAULT_MESSAGE = "Board cannot be null"


# ======================# BOARD VALIDATION EXCEPTIONS #======================#
class InvalidBoardException(BoardException, ValidationException):
    """Catchall Exception for BoardValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "BOARD_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Board validation failed."


class BoardNullPieceListException(BoardException, NullException):
    """Raised if a Board.pieces list does not exist. This should never happen."""
    ERROR_CODE = "MISSING_PIECES_LIST_ERROR"
    DEFAULT_MESSAGE = "The Board.pieces list is null. There may be a service failure or data inconsistency."


class BoardNullSquareListException(BoardException, NullException):
    """Raised if a Board.squares list does not exist. This should never happen."""
    ERROR_CODE = "BOARD_MISSING_SQUARE_LIST_ERROR"
    DEFAULT_MESSAGE = "The Board.squares list is null. There may be a service failure or data inconsistency."


class NumberOfBoardSquaresOutOfBoundsException(BoardException):
    """Raised if the Board does not contain 64 boards. This should never happen."""
    ERROR_CODE = "NUMBER_OF_BOARD_SQUARES_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The number of Square instance in Board is out of bounds. Only 64 Squares are allowed."


# ======================# BOARD BUILD EXCEPTIONS #======================#
class BoardBuildFailedException(BoardException, BuildFailedException):
    """Catchall Exception for DomainBuilder when it encounters an error building a Domain."""
    ERROR_CODE = "BOARD_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Board build failed."


# ======================# PIECE ADDITION/REMOVAL EXCEPTIONS WITH ROLLBACK #======================#
class FailedPieceAdditionRolledBackException(BoardException, RollbackException):
    """Raised after a Transaction rolled back changes when it could not add a Piece to a Board."""
    ERROR_CODE = "BOARD_PIECE_ADDITION_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Adding the Piece to the Board failed during the Transaction. The transaction was rolled back "
        "before raising this exception."
    )


class FailedPieceRemovalRolledBackException(BoardException, RollbackException):
    """Raised after a Transaction rolled back changes when it could not remove a Piece to a Board."""
    ERROR_CODE = "BOARD_PIECE_REMOVAL_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Removing the Piece to the Board failed during the Transaction. The transaction was rolled back "
        "before raising this exception."
    )


# ======================# BOARD CONSISTENCY EXCEPTION #======================#
class CoordSearchInvariantBreachException(BoardException, InvariantBreachException):
    """Raised if searching the board for a Coord in the legal range produces either no or many results."""
    DEFAULT_CODE = "BOARD_COORD_INVARIANT_BREACH_ERROR"
    DEFAULT_MESSAGE = (
        "The Board's Coord invariant was breached, There may be a critical state inconsistency. or service loss."
    )


class SquareInvariantBreachException(BoardException, InvariantBreachException):
    """Raised if searching the board for a Board in the legal range produces either no or many results."""
    DEFAULT_CODE = "BOARD_SQUARE_INVARIANT_BREACH_ERROR"
    DEFAULT_MESSAGE = (
        "The Board's Square invariant was breached, There may be a critical state inconsistency. or service loss."
    )
