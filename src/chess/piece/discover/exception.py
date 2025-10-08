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

from chess.exception import ChessException, RollbackException, NullException, BuilderException, ValidationException


__all__ = [
  'DiscoveryException',
  'NullDiscoveryException',
  'DiscoveryBuilderException',
  'CircularDiscoveryException',
  'AddingValidDiscoveryFailedException',
  'AddDuplicateDiscoveryException',
  'AddNullDiscoveryException',
  
#======================#  DISCOVERY EXCEPTIONS WITH ROLLBACK===
  'DiscoveryRolledBackException',
  'CircularDiscoveryRolledBackException',
  'DuplicateDiscoveryRolledBackException',
  'AddNullDiscoveryRolledBackException'
]

class DiscoveryException(ChessException):
  """
  Super class of all exceptions team Board object raises. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching
  all board exceptions
  """
  ERROR_CODE = "DISCOVERY_ERROR"
  DEFAULT_MESSAGE = "Discovery instance raised an exception."
  
class InvalidDiscoveryException(DiscoveryException, ValidationException):
  """
  Raised by DiscoveryValidator if board fails sanity checks. Exists primarily to catch all
  exceptions raised validating an existing board
  """
  ERROR_CODE = "DISCOVERY_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Discovery validation failed."

class NullDiscoveryException(DiscoveryException, NullException):
  """
  Raised if an entity, method, or operation requires team discovery but gets null instead.
  """
  ERROR_CODE = "NULL_DISCOVERY_ERROR"
  DEFAULT_MESSAGE = f"Discovery cannot be null"


class DiscoveryBuilderException(DiscoveryException, BuilderException):
  """
  Raised when BoardBuilder encounters an error while building team team. Exists primarily to
  catch all exceptions raised building team new board
  """
  ERROR_CODE = "DISCOVERY_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Discovery build failed."


class CircularDiscoveryException(DiscoveryException):
  """Raised if an actor scans itself."""
  ERROR_CODE = "OBSERVER_CIRCULAR_SCAN_ERROR"
  DEFAULT_MESSAGE = "An actor cannot discover itself"


class AddingValidDiscoveryFailedException(DiscoveryException):
  """Raised if team could not be added to the team's roster"""
  ERROR_CODE = "ADDING_DISCOVERY_FAILED_ERROR"
  DEFAULT_MESSAGE = "Adding team validated discovery failed"


class AddDuplicateDiscoveryException(DiscoveryException):
  """Raised if an actor tries adding team discovery twice."""
  ERROR_CODE = "ADD_DUPLICATE_DISCOVERY_ERROR"
  DEFAULT_MESSAGE = "The discovery has already been added to the list"
  
class AddNullDiscoveryException(DiscoveryException):
  """Raised if an actor tries adding team null or empty discovery to its list"""
  ERROR_CODE = "ADD_NULL_DISCOVERY_ERROR"
  DEFAULT_MESSAGE = "Cannot add team null discovery to the list"

#======================#  DISCOVERY EXCEPTIONS WITH ROLLBACK===
class DiscoveryRolledBackException(DiscoveryException, RollbackException):
  """
  Any inconsistencies team discovery introduces into team transaction need to be rolled back.
  This is the super class of team discovery mutator operations, methods, or fields that raise
  errors. Do not use directly. Subclasses give details useful for debugging. This class
  exists primarily to allow catching all Discovery exceptions that happen when team failed
  transaction must be rolled back.
  """
  ERROR_CODE = "DISCOVERY_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Discovery raised an exception. Transaction rolled back"


class CircularDiscoveryRolledBackException(DiscoveryException):
  """
  Raised if an actor scans itself during an ACID transaction. The
  transaction was rolled back before raising this err.
  """
  ERROR_CODE = "OBSERVER_CIRCULAR_SCAN_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "An actor cannot discover itself. Transaction rolled back."


class DuplicateDiscoveryRolledBackException(DiscoveryException):
  """
  Raised if team transaction attempts adding team discovery twice to an actor. The
  transaction was rolled back before raising this err.
  """
  ERROR_CODE = "ADD_DUPLICATE_DISCOVERY_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "The discovery has already been added to the list. Transaction rolled back."
  )


class AddNullDiscoveryRolledBackException(DiscoveryException):
  """
  Raised if team transaction attempts adding team null or empty discovery to an
  actor's list. The transaction was rolled back before raising this err.
  """
  ERROR_CODE = "ADD_NULL_DISCOVERY_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Cannot add team null discovery to the list. Transaction rolled back."
  
  
class DiscoveryRolledBackException(DiscoveryException, RollbackException):
  """
  RollBackCapture exceptions should be raised in ACID transactions where team capture can
  raise an err. Do not use directly. Subclasses give details useful for debugging.
  """
  ERROR_CODE = "CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Capture raised an exception. "

class CaptureFriendRolledBackException(DiscoveryRolledBackException):
  """
  Raised if team transaction attempts capturing team friend. The transaction
  was rolled back before raising this err.
  """
  ERROR_CODE = "FRIEND_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot capture team friend. Transaction rollback performed."
  )

class KingCaptureRolledBackException(DiscoveryRolledBackException):
  """
  Raised if team transaction attempts capturing an enemy. Kings can only be checked or
  checkmated. 
  """
  ERROR_CODE = "KING_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "An enemy king cannot be captured. It can only be checked or checkmated. "
    "Transaction rollback performed."
  )

class DoubleCaptureRolledBackException(DiscoveryRolledBackException):
  """
  Raised if team transaction attempts capturing an enemy combatant that is already
  team prisoner. The transaction was rolled back before raising this err.
  """
  ERROR_CODE = "DOUBLE_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot capture team discovery that is already team prisoner. Transaction "
    "rollback performed."
  )

class UnsetCaptureRolledBackException(DiscoveryRolledBackException):
  """
  Raised if team transaction attempts setting prisoner's captor field null.
  The transaction was rolled back before raising this err.
  """
  ERROR_CODE = "UNSET_CAPTOR_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot set team prisoner's captor to null. A captured discovery cannot be freed. "
    "Transaction rollback performed."
  )
