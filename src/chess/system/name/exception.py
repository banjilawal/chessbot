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

from chess.system import ChessException, NullException, ValidationException

__all__ = [
  'NullNameException',
  'LongNameException',
  'ShortNameException',
  'BlankNameException',
  'InvalidNameException',
]

from chess.system.err.exception import BlankStringException


class InvalidNameException(ValidationException):
  ERROR_CODE = "NAME_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"Name Validation failed"

class BlankNameException(InvalidNameException, BlankStringException):
  """
  Name with only white space raises BlankNameException
  """
  ERROR_CODE = "BLANK_NAME_ERROR"
  DEFAULT_MESSAGE = "Name cannot be white space only"


class ShortNameException(InvalidNameException):
  """
  Name below the minimum length raises ShortNameException. See documentation or
  chess.system.config for MIN_NAME_LENGTH.
  """
  ERROR_CODE = "SHORT_NAME_ERROR"
  DEFAULT_MESSAGE = "Name is below the minimum length"


class LongNameException(InvalidNameException):
  """
  Name is longer than MAX_NAME_LENGTH raises LongNameException. See documentation
  pr chess.system.config for MAX_NAME_LENGTH
  """
  ERROR_CODE = "LONG_NAME_ERROR"
  DEFAULT_MESSAGE = "Name is above the maximum length"


class NullNameException(InvalidNameException, NullException):
  """
  Raised if an entity's name is null
  """
  ERROR_CODE = "NULL_NAME_ERROR"
  DEFAULT_MESSAGE = f"Name cannot be null"

