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

from chess.exception import ChessException, NullException

__all__ = [
  'BuilderException',
  'NullBuilderException',
  'BuildFailedException',
  'AllParamsSetNullException',
  'MutuallyExclusiveParamsException'
]


class BuilderException(ChessException):
  """
  Super class of exceptions organic to `Builder` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `BuilderException` exists primarily to allow catching all `Builder`
  exceptions.
  """
  ERROR_CODE = "BUILDER_ERROR"
  DEFAULT_MESSAGE = "Builder raised an exception."

class NullBuilderException(BuilderException, NullException):
  """Raised if an entity, method, or operation requires a Engine but gets null instead."""
  ERROR_CODE = "NULL_ERROR"
  DEFAULT_MESSAGE = "Builder cannot be null"

class BuildFailedException(BuilderException):
  """
  Raised when a Builder encounters an error while building an object. Exists primarily to
  catch all exceptions raised building a new objects.
  """
  ERROR_CODE = "BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "build failed."

class AllParamsSetNullException(BuilderException):
  """
  Raised if all build params cannot be null.
  """
  ERROR_CODE = "ALL_PARAMS_SET_NULL_ERROR"
  DEFAULT_MESSAGE = "Cannot have all params set null."

class MutuallyExclusiveParamsException(BuilderException):
  """
  Raised if only one param cannot be null.
  """
  ERROR_CODE = "MUTUALLY_EXCLUSIVE_BUILD_PARAMS_ERROR"
  DEFAULT_MESSAGE = "Cannot have more than one param set null."



