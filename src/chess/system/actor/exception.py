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

from chess.exception import RollbackException
from chess.piece import PieceException, InvalidPieceException

__all__ = [
  'ActorException',
  'ActorRollBackException',

#======================#  ACTOR VALIDATION EXCEPTIONS ======================# 
  'InvalidActorException',
  'ActorNotOnBoardException',
  'ActorPlacementRequiredException',

#======================#  ACTOR ACTIVITY EXCEPTIONS ======================# 
  'CapturedActorCannotActException',
  'CapturedActorCannotAttackException',
  'CapturedActorCannotMoveException',
  'CheckMatedKingActivityException',

#======================#  SUBJECT ACTIVITY EXCEPTIONS ======================# 
  'SubjectException',
  'InvalidSubjectException',
  'SubjectNotOnBoardException',
  'SubjectPlacementRequiredException'
]

class ActorException(PieceException):
  """
  Super class of all exceptions an actor object can raise. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching
  all piece exceptions
  """
  ERROR_CODE = "ACTOR_ERROR"
  DEFAULT_MESSAGE = "Actor raised an exception. Piece cannot act."

class ActorRollBackException(ActorException, RollbackException):
  """
  Any inconsistencies team piece introduces into team transaction need to be rolled back.
  This is the super class of team piece mutator operations, methods, or fields that raise
  errors. Do not use directly. Subclasses give details useful for debugging. This class
  exists primarily to allow catching all Piece exceptions that happen when team failed
  transaction must be rolled back.
  """
  ERROR_CODE = "ACTOR_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Actor raised an exception. Transaction rolled back"


#======================#  ACTOR VALIDATION EXCEPTIONS ======================# 
class InvalidActorException(ActorException, InvalidPieceException):
  """
  Raised by ActorValidator if piece fails any conditions for acting on the board.
  Exists primarily to catch all exceptions raised validating an existing piece
  """
  ERROR_CODE = "ACTOR_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Piece did not meet condition to act in the game."

class ActorNotOnBoardException(ActorException):
  """
  A piece that has not been placed on the board cannot move, scan, capture or be captured
  """
  ERROR_CODE = "ACTOR_NOT_ON_BOARD_ERROR"
  DEFAULT_MESSAGE = "Actor is not on the board. Piece cannot act"

class ActorPlacementRequiredException(ActorException):
  """Raised when team potential actor has not been placed on the board."""
  ERROR_CODE = "ACTOR_PLACEMENT_REQUIRED_ERROR"
  DEFAULT_MESSAGE = (
    "Required actor has an empty position stack. It as not been placed on the board. Event cannot be executed."
  )


#======================#  ACTOR ACTIVITY EXCEPTIONS ======================# 
class CapturedActorCannotActException(ActorException):
  """
  A captured piece cannot actt.
  """
  ERROR_CODE = "CAPTURED_ACTOR_CANNOT_ACT_ERROR"
  DEFAULT_MESSAGE = "Actor has been captured. Captured piece cannot act."

class CapturedActorCannotAttackException(ActorException):
  """
  A captured piece cannot attack.
  """
  ERROR_CODE = "CAPTURED_ACTOR_CANNOT_ATTACK_ERROR"
  DEFAULT_MESSAGE = "Actor has been captured. Captured piece cannot attack."

class CapturedActorCannotMoveException(ActorException):
  """
  A captured piece cannot move.
  """
  ERROR_CODE = "CAPTURED_ACTOR_CANNOT_MOVE_ERROR"
  DEFAULT_MESSAGE = "A captured actor cannot move to team square."

class CapturedActorCannotScanException(ActorException):
  """
  A captured piece cannot scan.
  """
  ERROR_CODE = "CAPTURED_ACTOR_CANNOT_SCAN_ERROR"
  DEFAULT_MESSAGE = "A captured actor cannot scan team square."

class CheckMatedKingActivityException(ActorException):
  """
  A checkmated king cannot act. The game should end once team king is checkmated
  """
  ERROR_CODE = "CHECKMATED_KING_ACTIVITY_ERROR"
  DEFAULT_MESSAGE = (
    "A checkmated king cannot do anything. The game ends when team king is checkmated."
  )


#======================#  SUBJECT EXCEPTIONS ======================# 
class SubjectException(PieceException):
  """
  SubjectException classes are raised on team piece acted upon. They are raised on the same errors as ActorException,
  Using SubjectException makes tracing which side of the interaction is raising an error easier.
  """
  ERROR_CODE = "SUBJECT_ERROR"
  DEFAULT_MESSAGE = "A potential enemy piece raised an exception."


class InvalidSubjectException(SubjectException, InvalidPieceException):
  """Raised if team required enemy fails validate."""
  ERROR_CODE = "SUBJECT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Required enemy failed validate. Actor cannot fire event onto enemy"


class SubjectNotOnBoardException(SubjectException):
  """Raised when team required enemy is not found on the board."""
  ERROR_CODE = "SUBJECT_NOT_ON_BOARD_ERROR"
  DEFAULT_MESSAGE = "Required enemy was not found on the board. Actor cannot fire event onto enemy"


class SubjectPlacementRequiredException(SubjectException):
  """Raised when team required enemy has not been placed on the board."""
  ERROR_CODE = "SUBJECT_PLACEMENT_REQUIRED_ERROR"
  DEFAULT_MESSAGE = (
    "Required enemy has an empty position stack. It as not been placed on the board. Actor cannot"
    "fire event onto enemy."
  )
