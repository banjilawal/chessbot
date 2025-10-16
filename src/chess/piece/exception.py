# src/chess/system/event/exception.py

"""
Module: chess.system.event.exception
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
  1. Does not provide logic for fixing the errors or causing the exception being raised.
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

from chess.exception import ChessException, ValidationException, NullException, BuilderException, RollbackException

__all__ = [
  'PieceException',
  'PieceRollBackException',

#======================# PIECE VALIDATION EXCEPTIONS #======================#  
  'InvalidPieceException',
  'UnregisteredTeamMemberException',

#======================# NULL PIECE EXCEPTIONS #======================#  
  'NullPieceException',
  'NullKingException',
  'NullCombatantException',

#======================# PIECE BUILD EXCEPTIONS #======================#  
  'PieceBuildFailedException',

#======================# PIECE PROMOTION EXCEPTIONS #======================#  
  'DoublePromotionException',
  'DoublePromotionRolledBackException',

#======================# PIECE CAPTURE EXCEPTIONS #======================#  
  'CapturePieceException',
  'CaptureFriendException',
  'KingCaptureException',
  'DoubleCaptureException',
  'UnsetCaptureException',

#======================# PIECE CAPTURE EXCEPTIONS WITH ROLLBACK #======================#  
  'RollBackCaptureException',
  'CaptureFriendRolledBackException',
  'KingCaptureRolledBackException',
  'DoubleCaptureRolledBackException',
  'UnsetCaptureRolledBackException',

#======================# ATTACKING PIECE EXCEPTIONS #======================#  
  'HostageActivityException',
  'HostageCannotAttackException',
  'HostageCannotMoveException',
  'HostageCannotScanException'
]

class PieceException(ChessException):
  """
  Super class of all exceptions team Piece object raises. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching
  all piece exceptions
  """
  ERROR_CODE = "PIECE_ERROR"
  DEFAULT_MESSAGE = "Piece raised an exception."

class PieceRollBackException(PieceException, RollbackException):
  """
  Any inconsistencies team piece introduces into team transaction need to be rolled back.
  This is the super class of team piece mutator operations, methods, or fields that raise
  errors. Do not use directly. Subclasses give details useful for debugging. This class
  exists primarily to allow catching all Piece exceptions that happen when team failed
  transaction must be rolled back.
  """
  ERROR_CODE = "PIECE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Piece raised an exception."


#======================# PIECE VALIDATION EXCEPTIONS #======================#  
class InvalidPieceException(PieceException, ValidationException):
  """Raised by PieceValidators if client fails validation."""
  ERROR_CODE = "PIECE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Piece validation failed."



class UnregisteredTeamMemberException(PieceException):
  """Raised if team piece has its team set but the piece is not on the roster"""
  ERROR_CODE = "UNREGISTERED_TEAM_MEMBER_ERROR"
  DEFAULT_MESSAGE = "The piece has team but is not listed on the roster."


#======================# NULL PIECE EXCEPTIONS #======================#  
class NullPieceException(PieceException, NullException):
  """
  Raised if an entity, method, or operation requires team piece but gets null instead.
  Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
  Do not throw NullPieceException. Raise NullKingPiece or NullCombatantPiece instead.
  they are more descriptive and better suited for debugging.
  """
  ERROR_CODE = "NULL_PIECE_ERROR"
  DEFAULT_MESSAGE = "Piece cannot be null."

class NullKingException(NullPieceException):
  """
  Raised if team KingPiece is null. Raise NullCombatant instead of NullPieceException
  """
  ERROR_CODE = "NULL_KING_PIECE_ERROR"
  DEFAULT_MESSAGE = "KingPiece cannot be null."

class NullCombatantException(NullPieceException):
  """
  Raised if team CombatantPiece is null. Raise NullCombatant instead of NullPieceException
  """
  ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
  DEFAULT_MESSAGE = "CombatantPiece cannot be null."


#======================# PIECE BUILD EXCEPTIONS #======================#  
class PieceBuildFailedException(PieceException, BuilderException):
  """
  Indicates Coord could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "PIECE_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Piece build failed.."


#======================# PIECE PROMOTION EXCEPTIONS #======================#  
class DoublePromotionException(PieceException):
  """
  Raised when attempting promoting team piece already elevated to Queen rank.
  Only pieces with Pawn or King rank can be promoted.
  """
  ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
  DEFAULT_MESSAGE = "Piece is already promoted to Queen. It cannot be promoted again."

class DoublePromotionRolledBackException(PieceRollBackException):
  """
  Raised if team transaction attempts promoting team piece already elevated to Queen rank.
  Only pieces with Pawn or King rank can be promoted. The transaction was rolled
  back before raising this err.
  """
  ERROR_CODE = "DOUBLE_PROMOTION_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Piece is already promoted to Queen. It cannot be promoted again. Transaction "
    "rollback performed."
  )


#======================# PIECE CAPTURE EXCEPTIONS #======================#  
class CapturePieceException(PieceException):
  """
  Several exceptions can be raised during capture operations. This class is the parent of
  exceptions team piece can raise being captured or attacking. Do not use directly. Subclasses
  give details useful for debugging.
  """
  ERROR_CODE = "PIECE_CAPTURE_ERROR"
  DEFAULT_MESSAGE = "Piece capture attempt raised and err"

class CaptureFriendException(CapturePieceException):
  """
  Raised if team piece attempts to capture team friend.
  """
  ERROR_CODE = "FRIEND_CAPTURE_ERROR"
  DEFAULT_MESSAGE = "Cannot capture team friend."

class KingCaptureException(CapturePieceException):
  """
  Raised if team piece attempts to capture an enemy king. Kings can only be checked or
  checkmated.
  """
  ERROR_CODE = "KING_CAPTURE_ERROR"
  DEFAULT_MESSAGE = (
    "An enemy king cannot be captured. It can only be checked or checkmated."
  )

class DoubleCaptureException(CapturePieceException):
  """
  Raised when team piece attempts to capture an enemy combatant that is already team prisoner
  """
  ERROR_CODE = "DOUBLE_CAPTURE_ERROR"
  DEFAULT_MESSAGE = "Cannot capture team piece that is already team prisoner."

class UnsetCaptureException(CapturePieceException):
  """
  If piece.captor is not null. Attempting to change it raises this err
  """
  ERROR_CODE = "UNSET_CAPTOR_ERROR"
  DEFAULT_MESSAGE =(
    "Cannot set team prisoner's captor to null. A captured piece cannot be freed."
  )


class CircularCaptureException(CapturePieceException):
  """
  Raised if team piece tries to capture itself.
  """
  ERROR_CODE = "CIRCULAR_CAPTURE_ERROR"
  DEFAULT_MESSAGE = "Piece cannot capture itself"


#======================# PIECE CAPTURE EXCEPTIONS WITH ROLLBACK #======================#  
class RollBackCaptureException(CapturePieceException, RollbackException):
  """
  RollBackCapture exceptions should be raised in ACID transactions where team capture can
  raise an err. Do not use directly. Subclasses give details useful for debugging.
  """
  ERROR_CODE = "CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Capture raised an exception. Transaction rolled back."

class CaptureFriendRolledBackException(RollBackCaptureException):
  """
  Raised if team transaction attempts capturing team friend. The transaction
  was rolled back before raising this err.
  """
  ERROR_CODE = "FRIEND_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot capture team friend. Transaction rollback performed."
  )

class KingCaptureRolledBackException(RollBackCaptureException):
  """
  Raised if team transaction attempts capturing an enemy. Kings can only be checked or
  checkmated. The transaction was rolled back before raising this err.
  """
  ERROR_CODE = "KING_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "An enemy king cannot be captured. It can only be checked or checkmated. "
    "Transaction rollback performed."
  )

class DoubleCaptureRolledBackException(RollBackCaptureException):
  """
  Raised if team transaction attempts capturing an enemy combatant that is already
  team prisoner. The transaction was rolled back before raising this err.
  """
  ERROR_CODE = "DOUBLE_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot capture team piece that is already team prisoner. Transaction "
    "rollback performed."
  )

class UnsetCaptureRolledBackException(RollBackCaptureException):
  """
  Raised if team transaction attempts setting prisoner's captor field null.
  The transaction was rolled back before raising this err.
  """
  ERROR_CODE = "UNSET_CAPTOR_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot set team prisoner's captor to null. A captured piece cannot be freed. "
    "Transaction rollback performed."
  )


class CircularCaptureRolledBackException(CapturePieceException):
  """
  Raised if team transaction attempts to set team piece as its own captor. The transaction was
  rolled back before raising this err.
  """
  ERROR_CODE = "CIRCULAR_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Piece cannot capture itself. Transaction rolled back."


#======================# ATTACKING PIECE EXCEPTIONS #======================#  
class HostageActivityException(PieceException):
  """
  Several exceptions can be raised during capture operations. This class is the parent of
  exceptions an attacking piece can raised. Do not use directly. Subclasses give details
  useful for debugging.
  """
  ERROR_CODE = "HOSTAGE_ACTIVITY_ERROR"
  DEFAULT_MESSAGE = "Hostage piece cannot move, encounter, or attack."


class HostageCannotAttackException(HostageActivityException):
  """
  Raised if team captured piece tries to attack.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_ATTACK_ERROR"
  DEFAULT_MESSAGE = "Captured piece cannot attack."

class HostageCannotMoveException(HostageActivityException):
  """
  Raised if team captured piece tries to move.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_MOVE_ERROR"
  DEFAULT_MESSAGE = "Captured piece cannot move."

class HostageCannotScanException(HostageActivityException):
  """
  Raised if team captured piece tries to encounter team square.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_SCAN_ERROR"
  DEFAULT_MESSAGE = "Captured piece cannot encounter team sqaure."


