# src/chess.coord.exception.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide a
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected domain** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` domain.
It abstracts underlying Python exceptions into domain-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""

from chess.exception import ChessException, BuilderException, NullException, ValidationException

__all__ = [
  'SquareException',

# === SQUARE VALIDATION EXCEPTIONS ===
  'NullSquareException',
  'InvalidSquareException',

# === SQUARE BUILD EXCEPTIONS ===
  'SquareBuildFailed'
]

class SquareException(ChessException):
  """
  Super class of all exceptions a Square object raises. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching all
  square exceptions.
  """
  ERROR_CODE = "SQUARE_ERROR"
  DEFAULT_MESSAGE = "Square raised an exception."


# === SQUARE VALIDATION EXCEPTIONS ===
class NullSquareException(SquareException, NullException):
  """Raised if an entity, method, or operation requires a Square but gets null instead."""
  ERROR_CODE = "NULL_SQUARE_ERROR"
  DEFAULT_MESSAGE = "Square cannot be null."

class InvalidSquareException(SquareException, ValidationException):
  """
  Raised by SquareValidator if square fails sanity checks. Exists primarily to catch
  all exceptions raised validating an existing square
  """
  ERROR_CODE = "SQUARE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Square validate failed"


# === SQUARE BUILD EXCEPTIONS ===
class SquareBuildFailed(SquareException, BuilderException):
  """
  Raised when SquareBuilder encounters an error building a square. Exists primarily
  to catch all exceptions raised creating a new square
  """
  ERROR_CODE = "SQUARE_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Square build failed."
