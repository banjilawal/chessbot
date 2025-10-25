# src/chess/piece/travel/attack/travel/rollback_exception.py

"""
Module: chess.piece.travel.attack.travel.rollback_exception
Author: Banji Lawal
Created: 2025-10-18
version: 1.0.0
"""

from chess.system import ChessException, NullException, BuildFailedException


__all__ = [
  'AttackEventException',
  'NullAttackEventException',
  'PieceAttackingItSelfException',
  'AttackingFriendException',
  'AttackingEnemyKingException',
  'AttackingPieceMissingFromBoardException',
  'EnemyNotInExpectedSquareException',
  'DoublyAttackingPrisonerException',
]


class AttackEventException(ChessException):
  """
  Super class of all exceptions team Piece object raises. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching
  all piece exceptions
  """
  ERROR_CODE = "ATTACK_ERROR"
  DEFAULT_MESSAGE = "An attack raised an rollback_exception."


#======================# ATTACK_EVENT VALIDATION EXCEPTIONS #======================#
class InvalidAttackEventException(TravelEventException, ValidationException):
  ERROR_CODE = "ATTACK_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "AttackEvent validator failed."


class NullAttackEventException(AttackEventException, NullException):
  """
  Raised if an entity, method, or operation requires team piece but gets null instead.
  Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
  Do not throw NullAttackException. Raise NullKingPiece or NullCombatantPiece instead.
  they are more descriptive and better suited for debugging.
  """
  ERROR_CODE = "NULL_ATTACK_ERROR"
  DEFAULT_MESSAGE = "Attack cannot be null"


class PieceAttackingItSelfException(AttackEventException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_ITSELF_ERROR"
  DEFAULT_MESSAGE = "Piece cannot attack itself."

class AttackingFriendException(AttackEventException):
  """"""
  ERROR_CODE = "ATTACKING_FRIEND_ERROR"
  DEFAULT_MESSAGE = "A friend cannot be attacked."


class AttackingEnemyKingException(AttackEventException):
  """"""
  ERROR_CODE = "ATTACKING_ENEMY_KING_ERROR"
  DEFAULT_MESSAGE = "An enemy cannot be attacked. They can only be checked or checkmated."

class DoublyAttackingPrisonerException(AttackEventException):
  """"""
  ERROR_CODE = "DOUBLY_ATTACKING_PRISONER_ERROR"
  DEFAULT_MESSAGE = "Cannot attack an enemy that is already a prisoner."

class AttackingPieceMissingFromBoardException(AttackEventException):
  """"""
  ERROR_CODE = "ATTACKING_ENEMY_MISSING_FROM_BOARD_ERROR"
  DEFAULT_MESSAGE = "Cannot attack an enemy which is not on the board."

class EnemyNotInExpectedSquareException(AttackEventException):
  """"""
  ERROR_CODE = "ENEMY_NOT_IN_EXPECTED_SQUARE_ERROR"
  DEFAULT_MESSAGE = "Enemy is not in the expected square. There maybe inconsistent data."


#======================# ATTACK_EVENT BUILD EXCEPTIONS #======================#
class AttackEventBuildFailedException(AttackEventException, BuildFailedException):
  """
  Indicates Coord could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "ATTACK_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "KingCheckEvent build failed."


# ======================# PIECE CAPTURE EXCEPTIONS #======================#
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
  DEFAULT_MESSAGE = (
    "Cannot set team prisoner's captor to null. A captured piece cannot be freed."
  )


class PieceCapturingItSelfException(CapturePieceException):
  """"""
  ERROR_CODE = "PIECE_CAPTURING_IT_SELF_ERROR"
  DEFAULT_MESSAGE = "Piece cannot capture itself."


# ======================# PIECE CAPTURE EXCEPTIONS WITH ROLLBACK #======================#
class CaptureRollbackException(CapturePieceException, RollbackException):
  """
  RollBackCapture exceptions should be raised in ACID transactions where team capture can
  raise an err. Do not use directly. Subclasses give details useful for debugging.
  """
  ERROR_CODE = "CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Capture raised an rollback_exception. Transaction rolled back."


class CaptureFriendRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team notification attempts capturing team friend. The notification
  was rolled back before raising this err.
  """
  ERROR_CODE = "FRIEND_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot capture team friend. Transaction rollback performed."
  )


class DoubleCaptureRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team notification attempts capturing an enemy combatant that is already
  team prisoner. The notification was rolled back before raising this err.
  """
  ERROR_CODE = "DOUBLE_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot capture team piece that is already team prisoner. Transaction "
    "rollback performed."
  )


class UnsetCaptureRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team notification attempts setting prisoner's captor field null.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "UNSET_CAPTOR_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot set team prisoner's captor to null. A captured piece cannot be freed. "
    "Transaction rollback performed."
  )


class CapturingItSelfRolledBackException(CapturePieceException):
  """
  Raised if team notification attempts to set team piece as its own captor. The notification was
  rolled back before raising this err.
  """
  ERROR_CODE = "PIECE_CAPTURING_IT_SELF_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = "Piece attempted to capture itself during the notification. The notification was rolled back."


# ======================# PIECE CAPTURE EXCEPTIONS #======================#
class CapturePieceException(PieceException):
  """
  Several exceptions can be raised during capture operations. This class is the parent of
  exceptions team piece can raise being captured or attacking. Do not use directly. Subclasses
  give details useful for debugging.
  """
  ERROR_CODE = "PIECE_CAPTURE_ERROR"
  DEFAULT_MESSAGE = "Piece capture attempt raised and err"


class PieceAttackingFriendException(AttackEventException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_FRIEND_ERROR"
  DEFAULT_MESSAGE = "Piece cannot attack a friend."


class PieceAttackingKingException(AttackEventException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_KING_ERROR"
  DEFAULT_MESSAGE = "Piece cannot attack a king."


class PieceAttackingHostageException(AttackEventException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_HOSTAGE_ERROR"
  DEFAULT_MESSAGE = "Piece cannot attack a hostage."


class AttackingNullException(AttackEventException, NullException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_NULL_ERROR"
  DEFAULT_MESSAGE = "Piece cannot attack something null."


class HostageCannotAttackException(AttackEventException):
  """
  Raised if team captured piece tries to attack.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_ATTACK_ERROR"
  DEFAULT_MESSAGE = "Captured piece cannot attack."
