# src/chess/promotion/promotion/base.py

"""
Module: chess.promotion.promotion.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` integrity requirement.
  2. A satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module's only covers exceptions raised by `IdValidator`;

# SECTION 3: Limitations
  1. Does not provide logic for fixing the errors or causing the rollback_exception being raised.
       `IdValidator` is responsible for the logic which raises these exceptions.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. Discoverability.
  3. Encapsulations.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.


# SECTION 6 - Feature Delivery Mechanism:
1. Exceptions specific to verifying ids.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ChessException`, `ContextException`, `ResultException`

# SECTION 8 - Contains:
See the list of exceptions in the `__all__` list following (e.g., `EventException`,`TransactionException`).
"""

# src/chess/vector/rollback_exception.py

"""
Module: chess.vector.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, coord_stack_validator, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each consistency and behavior in the `Vector` class has an rollback_exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` graph.
2. Fast debugging using highly granular rollback_exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` graph.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationFailedException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
"""

from chess.event import EventException, TransactionException
from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
  'PromotionEventException',

#====================== PROMOTION_EVENT VALIDATION EXCEPTIONS #======================#  
  'NullPromotionEventException',
  'InvalidPromotionEventException',

#====================== PROMOTION_EVENT BUILD EXCEPTIONS #======================#  
  'PromotionEventBuildFailed',

#====================== PROMOTION_TRANSACTION EXCEPTIONS #======================#  
  'PromotionTransactionException',
  'NullPromotionTransactionException',
]

class PromotionEventException(ChessException):
  """
  Super class of exceptions organic to `PromotionEven` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `PromotionEventException` exists primarily to allow catching all `PromotionEven`
  exceptions.
  """
  ERROR_CODE = "PROMOTION_EVENT_ERROR"
  DEFAULT_MESSAGE = "PromotionEvent raised an rollback_exception."


#======================# PROMOTION_EVENT VALIDATION EXCEPTIONS #======================#  
class NullPromotionEventException(PromotionEventException, NullException):
  """Raised if an entity, method, or operation requires team_name `PromotionEvent` but gets null instead."""
  pass

class PawnPromotionOnlyException(PromotionEventException):
  """"""
  ERROR_CODE = "CAN_ONLY_PROMOTE_PAWN_ERROR"
  DEFAULT_MESSAGE = "Only pawns can be promoted"

class InvalidPromotionEventException(PromotionEventException, ValidationException):
  """
  Raised by PromotionEventValidator if team_name client fails sanity checks. Exists to catch all
  exceptions raised validating an existing `PromotionEvent` candidate.
  """
  ERROR_CODE = "PROMOTION_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "PromotionEvent validation failed."

class DoublePromotionException(PromotionEventException):
  """
  Raised when attempting promoting team_name owner already elevated to Queen bounds.
  Only pieces with Pawn or King bounds can be promoted.
  """
  ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
  DEFAULT_MESSAGE = "Piece is already promoted to Queen. It cannot be promoted again."


# ======================# PIECE PROMOTION EXCEPTIONS #======================#



class DoublePromotionRolledBackException(RollBackException):
  """
  Raised if team_name notification attempts promoting team_name owner already elevated to Queen bounds.
  Only pieces with Pawn or King bounds can be promoted. The notification was rolled
  back before raising this err.
  """
  ERROR_CODE = "DOUBLE_PROMOTION_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Piece is already promoted to Queen. It cannot be promoted again. Transaction "
    "rollback performed."
  )


# ======================# PIECE PROMOTION EXCEPTIONS #======================#
class DoublePromotionException(PieceException):
  """
  Raised when attempting promoting team_name owner already elevated to Queen bounds.
  Only pieces with Pawn or King bounds can be promoted.
  """
  ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
  DEFAULT_MESSAGE = "Piece is already promoted to Queen. It cannot be promoted again."


class DoublePromotionRolledBackException(PieceRollBackException):
  """
  Raised if team_name notification attempts promoting team_name owner already elevated to Queen bounds.
  Only pieces with Pawn or King bounds can be promoted. The notification was rolled
  back before raising this err.
  """
  ERROR_CODE = "DOUBLE_PROMOTION_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Piece is already promoted to Queen. It cannot be promoted again. Transaction "
    "rollback performed."
  )


#======================# PROMOTION_EVENT BUILD EXCEPTIONS #======================#  
class PromotionEventBuildFailed(PromotionEventException, BuildFailedException):
  """
  Raised when `PromotionEventBuilder` crashed while building team_name new `PromotionEven`. Exists
  primarily to catch all exceptions raised creating `PromotionEvent` objects.
  """
  ERROR_CODE = "PROMOTION_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "PromotionEvent build failed."


#======================# PROMOTION_TRANSACTION EXCEPTIONS #======================#  
class PromotionTransactionException(TransactionException):
  """
  Wraps any errors raised during the promotion's lifecycle.
  """
  ERROR_CODE = "PROMOTION_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "PromotionTransaction raised an rollback_exception."

class NullPromotionTransactionException(TransactionException):
  """Raised if an entity, method, or operation requires team_name `PromotionEvent` but gets null instead."""
  ERROR_CODE = "PROMOTION_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "PromotionTransaction raised an rollback_exception."


# src/chess.point.rollback_exception.py

"""
Module: chess.point.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, coord_stack_validator, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and validation checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team_name
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected graph** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` graph.
It abstracts underlying Python exceptions into graph-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationFailedException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""

from chess.exception import RollbackException
from chess.piece import AttackException, InvalidAttackException

__all__ = [
  'ActorException',
  'ActorRollBackException',
  
  # ======================# ACTOR VALIDATION EXCEPTIONS #======================#
  'InvalidActorException',
  'ActorNotOnBoardException',
  'ActorPlacementRequiredException',
  
  # ======================# ACTOR ACTIVITY EXCEPTIONS #======================#
  'CapturedPieceCannotActException',
  'CapturedActorCannotAttackException',
  'CapturedActorCannotMoveException',

  
  # ======================# SUBJECT ACTIVITY EXCEPTIONS #======================#
  'SubjectException',
  'InvalidSubjectException',
  'SubjectNotOnBoardException',
  'SubjectPlacementRequiredException'
]


class ActorException(AttackException):
  """
  Super class of all exceptions an actor_candidate object can raise. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching
  all owner exceptions
  """
  ERROR_CODE = "ACTOR_ERROR"
  DEFAULT_MESSAGE = "Actor raised an rollback_exception. Piece cannot act."


class ActorRollBackException(ActorException, RollbackException):
  """
  Any inconsistencies team_name owner introduces into team_name notification need to be rolled back.
  This is the super class of team_name owner mutator rollback, methods, or fields that raise
  errors. Do not use directly. Subclasses give details useful for debugging. This class
  exists primarily to allow catching all Piece exceptions that happen when team_name failed
  notification must be rolled back.
  """
  ERROR_CODE = "ACTOR_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Actor raised an rollback_exception. Transaction rolled back"


# ======================# ACTOR VALIDATION EXCEPTIONS #======================#
class InvalidActorException(ActorException, InvalidAttackException):
  """
  Raised by ActorValidator if owner fails any conditions for acting on the board_validator.
  Exists primarily to catch all exceptions raised validating an existing owner
  """
  ERROR_CODE = "ACTOR_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Piece did not meet condition to act in the game."


class ActorNotOnBoardException(ActorException):
  """
  A owner that has not been placed on the board_validator cannot move, blocking, capture or be captured
  """
  ERROR_CODE = "ACTOR_NOT_ON_BOARD_ERROR"
  DEFAULT_MESSAGE = "Actor is not on the board_validator. Piece cannot act"


class ActorPlacementRequiredException(ActorException):
  """Raised when team_name potential actor_candidate has not been placed on the board_validator."""
  ERROR_CODE = "ACTOR_PLACEMENT_REQUIRED_ERROR"
  DEFAULT_MESSAGE = (
    "Required actor_candidate has an empty position stack. It as not been placed on the board_validator. Event cannot be executed."
  )


# ======================# ACTOR ACTIVITY EXCEPTIONS #======================#
class CapturedPieceCannotActException(ActorException):
  """
  A captured owner cannot actt.
  """
  ERROR_CODE = "CAPTURED_ACTOR_CANNOT_ACT_ERROR"
  DEFAULT_MESSAGE = "Actor has been captured. Captured owner cannot act."


class CapturedActorCannotAttackException(ActorException):
  """
  A captured owner cannot attack.
  """
  ERROR_CODE = "CAPTURED_ACTOR_CANNOT_ATTACK_ERROR"
  DEFAULT_MESSAGE = "Actor has been captured. Captured owner cannot attack."


class CapturedActorCannotMoveException(ActorException):
  """
  A captured owner cannot move.
  """
  ERROR_CODE = "CAPTURED_ACTOR_CANNOT_MOVE_ERROR"
  DEFAULT_MESSAGE = "A captured actor_candidate cannot move to team_name square."


class CapturedActorCannotScanException(ActorException):
  """
  A captured owner cannot blocking.
  """
  ERROR_CODE = "CAPTURED_ACTOR_CANNOT_SCAN_ERROR"
  DEFAULT_MESSAGE = "A captured actor_candidate cannot blocking team_name square."





# ======================# SUBJECT EXCEPTIONS #======================#
class SubjectException(AttackException):
  """
  SubjectException classes are raised on team_name owner acted upon. They are raised on the same errors as ActorException,
  Using SubjectException makes tracing which side of the interaction is raising an error easier.
  """
  ERROR_CODE = "SUBJECT_ERROR"
  DEFAULT_MESSAGE = "A potential enemy owner raised an rollback_exception."


class InvalidSubjectException(SubjectException, InvalidAttackException):
  """Raised if team_name required enemy fails validate."""
  ERROR_CODE = "SUBJECT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Required enemy failed validate. Actor cannot fire travel onto enemy"


class SubjectNotOnBoardException(SubjectException):
  """Raised when team_name required enemy is not found on the board_validator."""
  ERROR_CODE = "SUBJECT_NOT_ON_BOARD_ERROR"
  DEFAULT_MESSAGE = "Required enemy was not found on the board_validator. Actor cannot fire travel onto enemy"


class SubjectPlacementRequiredException(SubjectException):
  """Raised when team_name required enemy has not been placed on the board_validator."""
  ERROR_CODE = "SUBJECT_PLACEMENT_REQUIRED_ERROR"
  DEFAULT_MESSAGE = (
    "Required enemy has an empty position stack. It as not been placed on the board_validator. Actor cannot"
    "fire travel onto enemy."
  )
