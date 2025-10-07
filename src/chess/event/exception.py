"""
Module: chess.event.err
Author: Banji Lawal
Created: 2025-10-01

# Purpose
Higher level exceptions raised by `Event` object and the `Transaction` classes managing `event` lifecycles.
Each Event and Transaction subclass has a corresponding Exception subclass, making debugging and maintenance
easier.

Contents:
  - `EventException:` Super class of all exceptions an event object raises.
  - `NullEventException:` Raised by methods, entities, and models that require an event but receive a null.
  - `InvalidEventException:` Super class of exceptions raised EventValidators raise if a client fails sanity checking.
  - `EventBuildFailedException:` Super class of exceptions raised when An EventBuilder runs into problems creating an event.
  - `TransactionException:` Super class of all exceptions a Transaction instances raise..

Notes:
  DO NOT USE THESE EXCEPTIONS DIRECTLY. Limited use in the finally statement of a try-except block.
"""
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

from chess.exception import ChessException, NullException, BuilderException

__all__ = [
  #=== AN EVENT EXCEPTIONS ===
  'EventException',
  'NullEventException',
  'InvalidEventException',
  'EventBuildFailedException',
  
  #=== TRANSACTION EXCEPTIONS ===
  'TransactionException'
]

from chess.system import ChessException, ValidationException, BuildFailedException, NullException,


#=== AN EVENT EXCEPTIONS ===
class EventException(ChessException):
  """
  Super class of all exceptions an event object raises. DO NOT USE DIRECTLY. Subclasses provide better
  debugging and maintenance support.

  Notes:
    Only use in the finally statement of a try-except block.
  """
  ERROR_CODE = "EVENT_ERROR"
  DEFAULT_MESSAGE = "Event raised an exception."

class NullEventException(EventException, NullException):
  """
  Raised by methods, entities, and models that require an event but receive a null.
  """
  ERROR_CODE = "NULL_EVENT_ERROR"
  DEFAULT_MESSAGE = "Event cannot be null."

class InvalidEventException(EventException, ValidationException):
  """
  Super class of exceptions raised EventValidators raise if a client fails sanity checking. Each EventValidator
  subclass has a corresponding InvalidEventException subclass, making debugging and maintenance easier.

  Notes:
    Only use in the finally statement of a try-except block.
  """
  ERROR_CODE = "INVALID_EVENT_ERROR"
  DEFAULT_MESSAGE = "Event validation failed."

class EventBuildFailedException(EventException, BuilderException):
  """
  Super class of exceptions raised when An EventBuilder runs into problems creating an event. Each EventBuilder
  subclass has a corresponding InvalidEventException subclass, making debugging and maintenance easier.

  Notes:
    Only use in the finally statement of a try-except block.
  """
  ERROR_CODE = "EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "EventBuilder validation failed."


 #=== TRANSACTION EXCEPTIONS ===

class TransactionException(ChessException):
  """
  Super class of all exceptions a Transaction instances raise. Do not use directly. Subclasses
  give details useful for debugging. Class exists primarily for catching all transaction exceptions.
  """
  ERROR_CODE = "TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "Transaction raised an exception."
