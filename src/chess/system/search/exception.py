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

from chess.system import ChessException

__all__ = [
  'SearchException',
  'SearchParamException',
  'ImpossibleFatalResultException'
]

class SearchException(ChessException):
  """
  Super class of exceptions organic to `Search` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `SearchException` exists primarily to allow catching all `Search`
  exceptions.
  """
  DEFAULT_CODE = "SEARCH_ERROR"
  DEFAULT_MESSAGE = "Search raised an exception."


class SearchParamException(SearchException):
  """
  This is different than failed validation checks. Might not be
  necessary.
  """
  DEFAULT_CODE = "SEARCH_PARAM_ERROR"
  DEFAULT_MESSAGE = "Search parameters raised an exception."


class ImpossibleFatalResultException(SearchException):
  """
  This is for sanity checking. Events and transactions need to ensure
  an `actor` and the `resource` they need to run a `Transaction` exist
  in the datapool in `SearchContext`. Validations and builds guarantee
  resources and actors exist in the game. If they are not found that
  indicates data inconsistency or nonexistent data pool.
  """
  DEFAULT_CODE = "IMPOSSIBLE_FATAL_RESULT_ERROR"
  DEFAULT_MESSAGE = (
    "The search result should be impossible. The result "
    "indicates a major data inconsistency or system error"
  )








