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

# chess.arena.exception

"""
Module: `chess.arena.exception`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
 Provides: Holds exceptions organic to `Arena` objects

Contains: See the list of exception in the __alL__ list following
"""

from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
  'ArenaException',

  # === ARENA VALIDATION EXCEPTIONS ===
  'NullArenaException',
  'InvalidArenaException',

  # === ARENA BUILD EXCEPTIONS ===
  'ArenaBuildFailedException',

  # === COLLECTION_ARENA EXCEPTIONS ===
]

class ArenaException(ChessException):
  """
  Super class exceptions Class object raises organically. Do not use directly. Subclasses give
  details useful for debugging. ClassException exists primarily to allow catching all class
  exceptions.
  """
  ERROR_CODE = "ARENA_ERROR"
  DEFAULT_MESSAGE = "Arena raised an exception."


# === ARENA VALIDATION EXCEPTIONS ===
class NullArenaException(ArenaException, NullException):
  """Raised if an entity, method, or operation requires an arena but gets null instead."""
  ERROR_CODE = "NULL_ARENA_ERROR"
  DEFAULT_MESSAGE = "Arena cannot be null"


class InvalidArenaException(ArenaException, ValidationException):
  """
  Raised by ArenaValidator if arena fails sanity checks. Exists primarily to
  catch all exceptions raised validating an existing arena
  """
  ERROR_CODE = "ARENA_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Arena validation failed"


# === ARENA BUILD EXCEPTIONS ===
class ArenaBuildFailedException(ArenaException, BuildFailedException):
  """
  Raised when ArenaBuilder crashed while building a new arena. Exists
  primarily to catch all exceptions raised creating arenas.
  """
  ERROR_CODE = "ARENA_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Arena build failed."