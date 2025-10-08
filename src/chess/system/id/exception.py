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
**Comprehensive Domain Error Catalog.** The central theme is to provide team
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

from chess.exception import ChessException, ValidationException, NullException

__all__ = [
  'IdNullException',
  'NegativeIdException',
  'InvalidIdException'
]

class InvalidIdException(ValidationException):
  ERROR_CODE = "ID_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"Id Validation failed"

class IdNullException(NullException):
  """
  Raised if an entity's id is null
  """
  ERROR_CODE = "NULL_ID_ERROR"
  DEFAULT_MESSAGE = f"Id cannot be null"


class NegativeIdException(ChessException):
  ERROR_CODE = "ID_IS_NEGATIVE"
  DEFAULT_MESSAGE = "Id cannot be negative"


