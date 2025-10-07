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
  'ScalarException',
  
#======================#  SCALAR VALIDATION EXCEPTIONS ======================# 
  'NullScalarException',
  'InvalidScalarException',
  
#======================#  SCALAR BUILD EXCEPTIONS ======================# 
  'ScalarBuildFailed',

#======================#  SCALAR BOUNDS EXCEPTIONS ======================# 
  'ScalarBelowBoundsException',
  'ScalarAboveBoundsException'
]

class ScalarException(ChessException):
  """
  Super class of all exceptions a Scalar object raises. Do not use directly. Subclasses 
  give details useful for debugging. This class exists primarily to allow catching all 
  Scalar exceptions.
  """
  ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
  DEFAULT_MESSAGE = "Scalar is below lower bound"
  

#======================#  SCALAR VALIDATION EXCEPTIONS ======================# 
class NullScalarException(ScalarException, NullException):
  """Raised if an entity, method, or operation requires a scalar but gets null instead."""
  ERROR_CODE = "NULL_SCALAR_ERROR"
  DEFAULT_MESSAGE = "Scalar cannot be null."

class InvalidScalarException(ScalarException, ValidationException):
  """Raised by ScalaValidators if client fails validation."""
  ERROR_CODE = "SCALAR_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Scalar validation failed."


#======================#  SCALAR BUILD EXCEPTIONS ======================# 
class ScalarBuildFailed(ScalarException, BuilderException):
  """
  Indicates Scalar could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "SCALAR_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Scalar build failed."


#======================#  SCALAR BOUNDS EXCEPTIONS ======================# 
class ScalarBelowBoundsException(ScalarException):
  """Raised if a scalar is below its < -KNIGHT_STEP_SIZE"""
  ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
  DEFAULT_MESSAGE = "Scalar cannot be less than -KNIGHT_STEP_SIZE."

class ScalarAboveBoundsException(ScalarException):
  """Raised if a scalar is above its > KNIGHT_STEP_SIZE"""
  ERROR_CODE = "SCALAR_UPPER_BOUND_ERROR"
  DEFAULT_MESSAGE = "Scalar cannot be greater than KNIGHT_STEP_SIZE."
