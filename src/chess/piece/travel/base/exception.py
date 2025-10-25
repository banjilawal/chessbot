# src/chess/piece/travel/base/exception.py

"""
Module: chess.piece.travel.base.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
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

from chess.system import (
  EventException, NullException, BuildFailedException, TransactionException, ValidationException,
  ResourceException, InconsistencyException
)

__all__ = [
  'TravelEventException',
  'TravelTransactionException',
]


class TravelEventException(EventException):
  ERROR_CODE = "TRAVEL_EXECUTION_ERROR"
  DEFAULT_MESSAGE = "TravelEvent raised an rollback_exception."
  
class TravelTransactionException(TransactionException):
  ERROR_CODE = "TRAVEL_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "An rollback_exception was raised during a TravelEvent."

#====================== TravelEvent VALIDATION EXCEPTIONS #======================#
class NullTravelEventException(TravelEventException, NullException):
  ERROR_CODE = "NULL_TRAVEL_EXECUTION_ERROR"
  DEFAULT_MESSAGE = "TravelEvent cannot be null."




#====================== TravelEvent BUILD EXCEPTIONS #======================#
class TravelEventBuildFailedException(TravelEventException, BuildFailedException):
  """
  Indicates TravelEvent could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "TRAVEL_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "TravelEvent build failed."

class OccupationEventBuildFailedException(TravelEventBuildFailedException):
  """
  Indicates OldOccupationEventValidator could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "OCCUPATION_EVENT_BUILD_FAILED_ERROR"

