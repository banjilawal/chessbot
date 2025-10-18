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
  'TransactionException',

  'FriendlyFireException',
  'AttackOnEmptySquareException',
  'EnemyNotOnBoardException',
  'NonCombatantTargetException',
  'KingTargetException',
  'AlreadyCapturedException',
  'MissingFromRosterException',
  'HostageTransferConflictException',
  'AutoCaptureException',


  'NullTransactionException',



]





class NullTransactionException(TransactionException, NullException):
  ERROR_CODE = "NULL_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "Transaction cannot be null"







class AutoCaptureException(CaptureContextException):
  ERROR_CODE = "NULL_CAPTURE_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "CaptureContext cannot be null"


class FriendlyFireException(CaptureContextException):
  DEFAULT_CODE = "FRIENDLY_FIRE"
  DEFAULT_MESSAGE = "Attempted to attack team friendly actor_candidate; this should not happen."


class AttackOnEmptySquareException(CaptureContextException):
  DEFAULT_CODE = "ATTACK_ON_EMPTY_SQUARE"
  DEFAULT_MESSAGE = "Attempted to attack an empty square; this should not happen."


class EnemyNotOnBoardException(CaptureContextException):
  DEFAULT_CODE = "ENEMY_NOT_ON_BOARD"
  DEFAULT_MESSAGE = "Attempted to capture team actor_candidate not present on the board_validator; this should not happen."


class NonCombatantTargetException(CaptureContextException):
  DEFAULT_CODE = "NON_COMBATANT_TARGET"
  DEFAULT_MESSAGE = "Attempted to capture team non-combatant actor_candidate; this should not happen."


class KingTargetException(CaptureContextException):
  DEFAULT_CODE = "KING_TARGET"
  DEFAULT_MESSAGE = "Attempted to capture team King actor_candidate; this should not happen."


class AlreadyCapturedException(CaptureContextException):
  DEFAULT_CODE = "ALREADY_CAPTURED"
  DEFAULT_MESSAGE = "Attempted to capture team actor_candidate that already has team captor; this should not happen."


class MissingFromRosterException(CaptureContextException):
  DEFAULT_CODE = "MISSING_FROM_ROSTER"
  DEFAULT_MESSAGE = "Expected actor_candidate not found in its team's roster; this should not happen."


class HostageTransferConflictException(CaptureContextException):
  DEFAULT_CODE = "HOSTAGE_TRANSFER_CONFLICT"
  DEFAULT_MESSAGE = "Piece already recorded in captor's hostage list; this should not happen."

