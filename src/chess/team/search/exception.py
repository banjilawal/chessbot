# src/chess.point.rollback_exception.py

"""
Module: chess.point.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, coord_stack_validator, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and validation checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team_name
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected graph** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` graph.
It abstracts underlying Python exceptions into graph-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""

"""
Result exceptions are about `Result` construction not the contents of the notification. A `ResultException` is
raised by `Builder` objects.
"""

from chess.exception import ChessException

__all__ = [
  'ResultException',
  'ResultConstructorException',
  'EmptyResultConstructorException',
  'ErrorContradictsPayloadException'
]

class ResultException(ChessException):
  """Base class for all Result exceptions"""
  ERROR_CODE = "RESULT_ERROR"
  DEFAULT_MESSAGE = "Result raised an rollback_exception."


class ResultConstructorException(ResultException):
  """Base class for all Result exceptions"""
  ERROR_CODE = "RESULT_CONSTRUCTOR_ERROR"
  DEFAULT_MESSAGE = "Invalid constructor params raised an rollback_exception."


class EmptyResultConstructorException(ResultConstructorException):
  ERROR_CODE = "EMPTY_RESULT_CONSTRUCTOR_ERROR"
  DEFAULT_MESSAGE = "A Result cannot be constructed with no payload or err."


class ErrorContradictsPayloadException(ResultConstructorException):
  """Raised if both payload and error params are not validation when constructing team_name Result object"""
  ERROR_CODE = "ERROR_CONFLICTS_PAYLOAD_IN_RESULT_CONSTRUCTOR"
  DEFAULT_MESSAGE = (
    "A Result cannot have both its payload and error set. Construct with either payload or err"
  )







