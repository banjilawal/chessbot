# src/chess/square/rollback_exception.py

"""
Module: chess.square.rollback_exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the ChessBot integrity requirement.
  2. A satisfaction of the ChessBot reliability requirement.

# SECTION 2 - Scope:
The module covers SquareValidator only.

# SECTION 3: Limitations
  1. Module ensures Square instances satisfy minimal requirements before use.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. Discoverability.
  3. Encapsulations.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.
  2. Ensuring validator results are communicated are sent to clients is an integrity feature.

# SECTION 6 - Feature Delivery Mechanism:
  1. Verify existing entities meet minimum requirements for use in the system.
  2. A description of an error condition, boundary violation, experienced or caused by an entity in
      the validator graph.
  3. The root of a scalable, modular hierarchy for validator related exceptions.

# SECTION 7 - Dependencies:
* From chess.system:
    ChessException

# SECTION 8 - Contains:
  * ValidationException
"""
"""
Module: chess.vector.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, validator, and manipulation of Vector objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
Vector, VectorBuilder, and VectorValidator

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each consistency and behavior in the Vector class has an rollback_exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the Vector graph.
2. Fast debugging using highly granular rollback_exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the Vector graph.
4. Providing a clear distinction between errors related to Vector instances and
    errors from Python, the Operating System or elsewhere in the ChessBot application.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From chess.system:
  * Exceptions: ChessException, ValidationException, NullException,
        BuildFailedException.

CONTAINS:
--------
See the list of exceptions in the __all__ list following (e.g., VectorException,
NullVectorException, InvalidVectorException, ).
"""

from chess.piece import PieceException
from chess.system import (
    ChessException, NullException, ValidationException, BuildFailedException, InconsistencyException
)

__all__ = [
    "SquareException",
    
# ======================# SQUARE VALIDATION EXCEPTIONS #======================#  
    "NullSquareException",
    "InvalidSquareException",
    
# ======================# SQUARE BUILD EXCEPTIONS #======================#  
    "SquareBuildFailedException",

# ======================# RELATIONAL SQUARE EXCEPTIONS #======================# 
    "SquareAndPieceMismatchedCoordException",
    "PieceInconsistentSquareOccupationException",
]


class SquareException(ChessException):
    """
    Super class of exceptions raised by a Square object. Do not use directly. Subclasses give
    targeted, fined grained, debugging info.
    """
    ERROR_CODE = "SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square raised an rollback_exception."


# ======================# SQUARE VALIDATION EXCEPTIONS #======================#  
class NullSquareException(SquareException, NullException):
    """Raised if an entity, method, or operation requires Square but gets null instead."""
    ERROR_CODE = "NULL_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square cannot be null."


class InvalidSquareException(SquareException, ValidationException):
    """Catchall Exception for SquareValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "SQUARE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Square validation failed."


# ======================# SQUARE BUILD EXCEPTIONS #======================# 
class SquareBuildFailedException(SquareException, BuildFailedException):
    """Catchall Exception for SquareBuilder when it encounters an error building a Square."""
    ERROR_CODE = "SQUARE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Square build failed."


# ======================# RELATIONAL SQUARE EXCEPTIONS #======================# 
class SquareAndPieceMismatchedCoordException(SquareException, PieceException):
    """Raised if a Piece needs to occupy a Square before they are used together."""
    ERROR_CODE = "SQUARE_AND_PIECE_COORD_MISMATCH_ERROR"
    DEFAULT_MESSAGE = "Square and Piece do not share a coord. They do not have a relationship."


class PieceInconsistentSquareOccupationException(SquareException, PieceException, InconsistencyException):
    """Raised if a Piece with the same Coord as a Square is not set as the Square\'s occupant"""
    ERROR_CODE = "PIECE_INCONSISTENT_SQUARE_OCCUPATION_ERROR"
    DEFAULT_MESSAGE = (
        "A Piece sharing a Coord with a Square is not marked as the Square\'s occupant. There may be "
        "service or data inconsistency."
    )
