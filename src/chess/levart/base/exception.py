# src/chess/owner/travel/base/collision.py

"""
Module: chess.owner.travel.base.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, coord_stack_validator, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and validation checks. It does not contain any logic for *raising* these exception; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Persona.** The central theme is to provide team_name
highly granular and hierarchical set of exception, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected graph** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` graph.
It abstracts underlying Python exception into graph-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Constants: `NUMBER_OF_ROWS`, `NUMBER_OF_COLUMNS`
  * Exception: `ChessException`, `ValidationFailedException`, `NullException`,
        `BuildException`.

CONTAINS:
--------
See the list of exception in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""

from chess.system import (
    EventException, NullException, BuildException, TransactionException, ValidationException,
    ResourceException, InconsistencyException
)

__all__ = [
  'TravelEventException',
  'TravelTransactionException',
]


class TravelEventException(EventException):
  ERROR_CODE = "TRAVEL_EXECUTION_ERROR"
  DEFAULT_MESSAGE = "TravelEvent raised an exception."
  
class TravelTransactionException(TransactionException):
  ERROR_CODE = "TRAVEL_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "An rollback_exception was raised during a TravelEvent."

#====================== TravelEvent VALIDATION EXCEPTION #======================#
class NullTravelEventException(TravelEventException, NullException):
  ERROR_CODE = "NULL_TRAVEL_EXECUTION_ERROR"
  DEFAULT_MESSAGE = "TravelEvent cannot be null."




#====================== TravelEvent BUILD EXCEPTION #======================#
class TravelEventBuildException(TravelEventException, BuildException):
  """
  Indicate That  TravelEvent could not be built. Wraps and re-raises errors that occurred
  during builder.
  """
  ERROR_CODE = "TRAVEL_EVENT_BUILD_FAILED"
  DEFAULT_MESSAGE = "TravelEvent build failed."

class OccupationEventBuildFailedException(TravelEventBuildException):
  """
  Indicate That  OldOccupationEventValidator could not be built. Wraps and re-raises errors that occurred
  during builder.
  """
  ERROR_CODE = "OCCUPATION_EVENT_BUILD_FAILED"

