# src/chess/owner/travel/attack/travel/rollback_exception.py

"""
Module: chess.owner.travel.attack.travel.rollback_exception
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
  Super class of all exception team_name Token object raises. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching
  all owner exception
  """
  ERROR_CODE = "ATTACK_ERROR"
  DEFAULT_MESSAGE = "An attack raised an exception."


#======================# ATTACK_EVENT VALIDATION EXCEPTION #======================#
class InvalidAttackEventException(TravelEventException, ValidationException):
  ERROR_CODE = "ATTACK_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "AttackEvent validation failed."


class NullAttackEventException(AttackEventException, NullException):
  """
  Raised if an entity, method, or operation requires team_name owner but gets validation instead.
  Token is an abstract method. KingPiece and CombatantPiece are its subclasses.
  Do not throw NullAttackException. Raise NullKingPiece or NullCombatantPiece instead.
  they are more descriptive and better suited for debugging.
  """
  ERROR_CODE = "NULL_ATTACK_ERROR"
  DEFAULT_MESSAGE = "Attack cannot be validation"


class PieceAttackingItSelfException(AttackEventException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_ITSELF_ERROR"
  DEFAULT_MESSAGE = "Token cannot attack itself."

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
  DEFAULT_MESSAGE = "Cannot attack an enemy that is already a combatant."

class AttackingPieceMissingFromBoardException(AttackEventException):
  """"""
  ERROR_CODE = "ATTACKING_ENEMY_MISSING_FROM_BOARD_ERROR"
  DEFAULT_MESSAGE = "Cannot attack an enemy which is not on the board."

class EnemyNotInExpectedSquareException(AttackEventException):
  """"""
  ERROR_CODE = "ENEMY_NOT_IN_EXPECTED_SQUARE_ERROR"
  DEFAULT_MESSAGE = "Enemy is not in the expected square_name. There maybe inconsistent entity_service."


#======================# ATTACK_EVENT BUILD EXCEPTION #======================#
class AttackEventBuildFailedException(AttackEventException, BuildFailedException):
  """
  Indicate That  Coord could not be built. Wraps and re-raises errors that occurred
  during builder.
  """
  ERROR_CODE = "ATTACK_EVENT_BUILD_FAILED"
  DEFAULT_MESSAGE = "KingCheckEvent build failed."


#======================# PIECE CAPTURE EXCEPTION #======================#
class CapturePieceException(PieceException):
  """
  Several exception can be raised during capture rollback. This class is the parent of
  exception team_name owner can raise being captured or attacking. Do not use directly. Subclasses
  give details useful for debugging.
  """
  ERROR_CODE = "PIECE_CAPTURE_ERROR"
  DEFAULT_MESSAGE = "Token capture attempt raised and err"


class CaptureFriendException(CapturePieceException):
  """
  Raised if team_name owner attempts to capture team_name friend.
  """
  ERROR_CODE = "FRIEND_CAPTURE_ERROR"
  DEFAULT_MESSAGE = "Cannot capture team_name friend."


class DoubleCaptureException(CapturePieceException):
  """
  Raised when team_name owner attempts to capture an enemy combatant that is already team_name combatant
  """
  ERROR_CODE = "DOUBLE_CAPTURE_ERROR"
  DEFAULT_MESSAGE = "Cannot capture team_name owner that is already team_name combatant."


class UnsetCaptureException(CapturePieceException):
  """
  If owner.captor is not validation. Attempting to change it raises this err
  """
  ERROR_CODE = "UNSET_CAPTOR_ERROR"
  DEFAULT_MESSAGE = (
    "Cannot set team_name combatant's captor to validation. A captured owner cannot be freed."
  )


class PieceCapturingItSelfException(CapturePieceException):
  """"""
  ERROR_CODE = "PIECE_CAPTURING_IT_SELF_ERROR"
  DEFAULT_MESSAGE = "Token cannot capture itself."


#======================# PIECE CAPTURE EXCEPTION WITH ROLLBACK #======================#
class CaptureRollbackException(CapturePieceException, RollbackException):
  """
  RollBackCapture exception should be raised in ACID transactions where team_name capture can
  raise an err. Do not use directly. Subclasses give details useful for debugging.
  """
  ERROR_CODE = "CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Capture raised an rollback_exception. Transaction rolled back."


class CaptureFriendRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team_name notification attempts capturing team_name friend. The notification
  was rolled back before raising this err.
  """
  ERROR_CODE = "FRIEND_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot capture team_name friend. Transaction rollback performed."
  )


class DoubleCaptureRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team_name notification attempts capturing an enemy combatant that is already
  team_name combatant. The notification was rolled back before raising this err.
  """
  ERROR_CODE = "DOUBLE_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot capture team_name owner that is already team_name combatant. Transaction "
    "rollback performed."
  )


class UnsetCaptureRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team_name notification attempts setting combatant's captor consistency validation.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "UNSET_CAPTOR_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot set team_name combatant's captor to validation. A captured owner cannot be freed. "
    "Transaction rollback performed."
  )


class CapturingItSelfRolledBackException(CapturePieceException):
  """
  Raised if team_name notification attempts to set team_name owner as its own captor. The notification was
  rolled back before raising this err.
  """
  ERROR_CODE = "PIECE_CAPTURING_IT_SELF_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = "Token attempted to capture itself during the notification. The notification was rolled back."


#======================# PIECE CAPTURE EXCEPTION #======================#



class PieceAttackingFriendException(AttackEventException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_FRIEND_ERROR"
  DEFAULT_MESSAGE = "Token cannot attack a friend."


class PieceAttackingKingException(AttackEventException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_KING_ERROR"
  DEFAULT_MESSAGE = "Token cannot attack a occupation."


class PieceAttackingHostageException(AttackEventException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_HOSTAGE_ERROR"
  DEFAULT_MESSAGE = "Token cannot attack a hostage."


class AttackingNullException(AttackEventException, NullException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_NULL_ERROR"
  DEFAULT_MESSAGE = "Token cannot attack something validation."


class HostageCannotAttackException(AttackEventException):
  """
  Raised if team_name captured owner tries to attack.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_ATTACK_ERROR"
  DEFAULT_MESSAGE = "Captured owner cannot attack."
