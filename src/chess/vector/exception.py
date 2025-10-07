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

from chess.exception import ChessException, NullException, ValidationException, BuilderException

__all__ = [
  'VectorException',

  # === VECTOR VALIDATION EXCEPTIONS ===
  'NullVectorException',
  'InvalidVectorException',

  # === VECTOR BUILD EXCEPTIONS ===
  'VectorBuilderException',

  # === NULL COMPONENT EXCEPTIONS ===
  'VectorAboveBoundsException',
  'VectorBelowBoundsException',

  # === VECTOR BOUNDS EXCEPTIONS ===
  'NullXComponentException',
  'NullYComponentException',
]

class VectorException(ChessException):
  """
  Super class of all exceptions a Vector object raises. Do not use directly. Subclasses give details useful
  for debugging. This class exists primarily to allow catching all vector exceptions
  """
  ERROR_CODE = "VECTOR_ERROR"
  DEFAULT_MESSAGE = "Vector raised an exception."


# === VECTOR VALIDATION EXCEPTIONS ===
class NullVectorException(VectorException, NullException):
  """Raised if an entity, method, or operation requires a vector but gets null instead."""
  ERROR_CODE = "NULL_VECTOR_ERROR"
  DEFAULT_MESSAGE = f"Vector cannot be null"


class InvalidVectorException(VectorException, ValidationException):
  """
  Raised by VectorValidator if vector fails sanity checks. Exists primarily to catch all exceptions raised
  validating an existing vector
  """
  ERROR_CODE = "VECTOR_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"Vector validation failed"


# === VECTOR BUILD EXCEPTIONS ===
class VectorBuilderException(VectorException, BuilderException):
  """
  Raised when VectorBuilder encounters an error while building a team. Exists primarily to catch all exceptions
  raised build a new vector
  """
  ERROR_CODE = "VECTOR_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Vector build failed."


# === NULL COMPONENT EXCEPTIONS ===
class NullXComponentException(VectorException, NullException):
  """Raised if a vector's x dimension is null"""
  ERROR_CODE = "VECTOR_NULL_X_DIMENSION_ERROR"
  DEFAULT_MESSAGE = f"Vector's X-dimension cannot be null"


class NullYComponentException(VectorException, NullException):
  """Raised if a vector's y dimension is null"""
  ERROR_CODE = "VECTOR_NULL_Y_DIMENSION_ERROR"
  DEFAULT_MESSAGE = f"Vector's Y-dimension cannot be null"


# === VECTOR BOUNDS EXCEPTIONS ===
class VectorAboveBoundsException(VectorException):
  """
  Iterating across coordinates to examine squares chess pieces can explore their with a step no
  larger than the knight's number of rows o squares covered in a move. If a vector's x value is
  larger than KNIGHT SIZE raise this err
  """
  ERROR_CODE = "VECTOR_ABOVE_BOUNDS"
  DEFAULT_MESSAGE = "Vector above bounds"


class VectorBelowBoundsException(VectorException):
  """
  Iterating across coordinates to examine squares chess pieces can explore their with a step no
  larger than the knight's number of rows o squares covered in a move. If a vector's x value is
  larger than KNIGHT SIZE raise this err
  """
  ERROR_CODE = "VECTOR_BELOW_BOUNDS_EXCEPTION"
  DEFAULT_MESSAGE = "Vector is below bounds"






