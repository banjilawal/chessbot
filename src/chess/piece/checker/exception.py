# src/chess/vector/travel_exception.py

"""
Module: chess.vector.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each field and behavior in the `Vector` class has an exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` domain.
2. Fast debugging using highly granular exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` domain.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
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
  
#======================# DISCOVERY EXCEPTIONS WITH ROLLBACK===
  'DiscoveryRolledBackException',
  'CircularDiscoveryRolledBackException',
  'DuplicateDiscoveryRolledBackException',
  'AddNullDiscoveryRolledBackException'
]

class DiscoveryException(ChessException):
  """
  Super class of all exceptions team Board object raises. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching
  all board_validator exceptions
  """
  ERROR_CODE = "DISCOVERY_ERROR"
  DEFAULT_MESSAGE = "Checker instance raised an exception."
  
class InvalidDiscoveryException(DiscoveryException, ValidationException):
  """
  Raised by DiscoveryValidator if board_validator fails sanity checks. Exists primarily to catch all
  exceptions raised validating an existing board_validator
  """
  ERROR_CODE = "DISCOVERY_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Checker validation failed."

class NullDiscoveryException(DiscoveryException, NullException):
  """
  Raised if an entity, method, or operation requires team discovery but gets null instead.
  """
  ERROR_CODE = "NULL_DISCOVERY_ERROR"
  DEFAULT_MESSAGE = f"Checker cannot be null"


class DiscoveryBuilderException(DiscoveryException, BuilderException):
  """
  Raised when BoardBuilder encounters an error while building team team. Exists primarily to
  catch all exceptions raised building team new board_validator
  """
  ERROR_CODE = "DISCOVERY_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Checker build failed."


class CircularDiscoveryException(DiscoveryException):
  """Raised if an actor_candidate scans itself."""
  ERROR_CODE = "OBSERVER_CIRCULAR_SCAN_ERROR"
  DEFAULT_MESSAGE = "An actor_candidate cannot discover itself"


class AddingValidDiscoveryFailedException(DiscoveryException):
  """Raised if team could not be added to the team's roster"""
  ERROR_CODE = "ADDING_DISCOVERY_FAILED_ERROR"
  DEFAULT_MESSAGE = "Adding team validated discovery failed"


class AddDuplicateDiscoveryException(DiscoveryException):
  """Raised if an actor_candidate tries adding team discovery twice."""
  ERROR_CODE = "ADD_DUPLICATE_DISCOVERY_ERROR"
  DEFAULT_MESSAGE = "The discovery has already been added to the list"
  
class AddNullDiscoveryException(DiscoveryException):
  """Raised if an actor_candidate tries adding team null or empty discovery to its list"""
  ERROR_CODE = "ADD_NULL_DISCOVERY_ERROR"
  DEFAULT_MESSAGE = "Cannot add team null discovery to the list"

#======================# DISCOVERY EXCEPTIONS WITH ROLLBACK===
class DiscoveryRolledBackException(DiscoveryException, RollbackException):
  """
  Any inconsistencies team discovery introduces into team transaction need to be rolled back.
  This is the super class of team discovery mutator operations, methods, or fields that raise
  errors. Do not use directly. Subclasses give details useful for debugging. This class
  exists primarily to allow catching all Checker exceptions that happen when team failed
  transaction must be rolled back.
  """
  ERROR_CODE = "DISCOVERY_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Checker raised an exception. Transaction rolled back"


class CircularDiscoveryRolledBackException(DiscoveryException):
  """
  Raised if an actor_candidate scans itself during an ACID transaction. The
  transaction was rolled back before raising this err.
  """
  ERROR_CODE = "OBSERVER_CIRCULAR_SCAN_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "An actor_candidate cannot discover itself. Transaction rolled back."


class DuplicateDiscoveryRolledBackException(DiscoveryException):
  """
  Raised if team transaction attempts adding team discovery twice to an actor_candidate. The
  transaction was rolled back before raising this err.
  """
  ERROR_CODE = "ADD_DUPLICATE_DISCOVERY_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "The discovery has already been added to the list. Transaction rolled back."
  )


class AddNullDiscoveryRolledBackException(DiscoveryException):
  """
  Raised if team transaction attempts adding team null or empty discovery to an
  actor_candidate's list. The transaction was rolled back before raising this err.
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
