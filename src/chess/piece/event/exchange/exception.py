# src/chess/vector/exception.py

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

from chess.exception import RollbackException
from chess.piece.event import OccupationEventException

__all__ = [
  #=== SCAN_TRANSACTION EXCEPTIONS ======================# 
  'ScanTransactionException',
  'NullScanTransactionException',

  #=== SCAN_EVENT EXCEPTIONS ======================# 
  'ScanEventException',
  'InvalidScanEventException',
  'NullScanEventException',

  #=== SCAN_EVENT BUILD EXCEPTIONS ======================# 
  'ScanEventBuilderException',
  'ScanSubjectException',
]


__all__ = [
  'AttackEventException',

  # Specific attack errors (no rollback)
  'UnexpectedNullEnemyException',


  # Rollback attack errors (dual inheritance)
  'RosterRemovalRollbackException',
  'HostageAdditionRollbackException',
  'BoardPieceRemovalRollbackException',
  'SquareOccupationRollbackException',
  'SourceSquareRollbackException',
  'PositionUpdateRollbackException',
]

#=== SCAN TRANSACTION EXCEPTIONS ======================# 
class ScanTransactionException(TransactionException):
  """
  Wraps any ScanEventExceptions or other errors raised during
  the scan's lifecycle.
  """
  ERROR_CODE = "SCAN_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "ScanTransaction raised an exception."



#=== SCAN_EVENT EXCEPTIONS ======================# 
class AttackEventException(OccupationEventException):
  """
  Base class for exceptions raised during attack/capture operations.

  PURPOSE:
    Used when an error occurs in the course of an attack or capture
    (e.g., invalid target, rollback during capture, inconsistent board state).
  """
  DEFAULT_CODE = "ATTACK_ERROR"
  DEFAULT_MESSAGE = "An error occurred during an attack or capture transaction."



#=== ATTACK_EVENT VALIDATION EXCEPTIONS ======================# 
class NullAttackEventException(AttackEventException, NullException):
  """Raised by methods, entities, and models that require team AttackEvent but receive team null."""
  ERROR_CODE = "NULL_EVENT_ERROR"
  DEFAULT_MESSAGE = "AttackEvent cannot be null"

class InvalidAttackEventException(AttackEventException, ValidationException):
  """Raised by ExchangeValidators if client fails validation."""
  ERROR_CODE = "ATTACK_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "AttackEvent failed validate"


#=== ATTACK_EVENT BUILD EXCEPTIONS ======================# 
class AttackEventBuilderException(AttackEventException, BuilderException):
  """
  Indicates Coord could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "ATTACK_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "AttackEventBuilder failed to create team AttackEvent"


#=== ATTACK_EVENT BUILD EXCEPTIONS ======================# 
class UnexpectedNullEnemyException(AttackEventException):
  DEFAULT_CODE = "UNEXPECTED_NULL_ENEMY"
  DEFAULT_MESSAGE = "Target actor is unexpectedly null during capture; this should not happen."





# --- Rollback Attack Errors (Dual Inheritance) ---
class SetCaptorRolledBackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SET_CAPTOR_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Setting captor failed. Transaction rolled back performed."


class EmptyDestinationSquareRolledBackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SET_CAPTOR_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Setting captor failed. Transaction rolled back performed."


class RosterRemovalRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "ROSTER_REMOVAL_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to remove actor from enemy roster after assigning captor; rollback performed."


class HostageAdditionRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "HOSTAGE_ADDITION_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to add captured actor to captor's hostage list; rollback performed."


class BoardPieceRemovalRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "BOARD_REMOVAL_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to remove captured actor from board; rollback performed."


class SquareOccupationRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SQUARE_OCCUPATION_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to occupy target square after capture; rollback executed."


class SourceSquareRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SOURCE_SQUARE_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to clear attacker's source square; rollback executed."


class PositionUpdateRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "POSITION_UPDATE_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to update actor's position history after move; rollback executed."
