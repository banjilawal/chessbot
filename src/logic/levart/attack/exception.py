# src/logic/owner/travel/attack/travel/rollback_exception.py

"""
Module: logic.owner.travel.attack.travel.rollback_exception
Author: Banji Lawal
Created: 2025-10-18
version: 1.0.0
"""

from logic.system import ChessException, NullException, BuildException


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
  ERR_CODE = "ATTACK_EXCEPTION"
  MSG = "An attack raised an exception."


#======================# ATTACK_EVENT VALIDATION EXCEPTION #======================#
class InvalidAttackEventException(TravelEventException, ValidationException):
  ERR_CODE = "ATTACK_EVENT_VALIDATION_EXCEPTION"
  MSG = "AttackEvent validation failed."


class NullAttackEventException(AttackEventException, NullException):
  """
  Raised if an entity, method, or operation requires team_name owner but gets validation instead.
  Token is an abstract method. KingPiece and CombatantPiece are its subclasses.
  Do not throw NullAttackException. Raise NullKingPiece or NullCombatantPiece instead.
  they are more descriptive and better suited for debugging.
  """
  ERR_CODE = "NULL_ATTACK_EXCEPTION"
  MSG = "Attack cannot be validation"


class PieceAttackingItSelfException(AttackEventException):
  """"""
  ERR_CODE = "PIECE_ATTACKING_ITSELF_EXCEPTION"
  MSG = "Token cannot attack itself."

class AttackingFriendException(AttackEventException):
  """"""
  ERR_CODE = "ATTACKING_FRIEND_EXCEPTION"
  MSG = "A friend cannot be attacked."


class AttackingEnemyKingException(AttackEventException):
  """"""
  ERR_CODE = "ATTACKING_ENEMY_KING_EXCEPTION"
  MSG = "An enemy cannot be attacked. They can only be checked or checkmated."

class DoublyAttackingPrisonerException(AttackEventException):
  """"""
  ERR_CODE = "DOUBLY_ATTACKING_PRISONER_EXCEPTION"
  MSG = "Cannot attack an enemy that is already a combatant."

class AttackingPieceMissingFromBoardException(AttackEventException):
  """"""
  ERR_CODE = "ATTACKING_ENEMY_MISSING_FROM_BOARD_EXCEPTION"
  MSG = "Cannot attack an enemy which is not on the board."

class EnemyNotInExpectedSquareException(AttackEventException):
  """"""
  ERR_CODE = "ENEMY_NOT_IN_EXPECTED_SQUARE_EXCEPTION"
  MSG = "Enemy is not in the expected square_name. There maybe inconsistent entity_service."


#======================# ATTACK_EVENT BUILD EXCEPTION #======================#
class AttackEventBuildException(AttackEventException, BuildException):
  """
  Indicate That  Coord could not be built. Wraps and re-raises errors that occurred
  during builder.
  """
  ERR_CODE = "ATTACK_EVENT_BUILD_FAILED"
  MSG = "KingCheckEvent build failed."


#======================# PIECE CAPTURE EXCEPTION #======================#
class CapturePieceException(PieceException):
  """
  Several exception can be raised during capture rollback. This class is the parent of
  exception team_name owner can raise being captured or attacking. Do not use directly. Subclasses
  give details useful for debugging.
  """
  ERR_CODE = "PIECE_CAPTURE_EXCEPTION"
  MSG = "Token capture attempt raised and err"


class CaptureFriendException(CapturePieceException):
  """
  Raised if team_name owner attempts to capture team_name friend.
  """
  ERR_CODE = "FRIEND_CAPTURE_EXCEPTION"
  MSG = "Cannot capture team_name friend."


class DoubleCaptureException(CapturePieceException):
  """
  Raised when team_name owner attempts to capture an enemy combatant that is already team_name combatant
  """
  ERR_CODE = "DOUBLE_CAPTURE_EXCEPTION"
  MSG = "Cannot capture team_name owner that is already team_name combatant."


class UnsetCaptureException(CapturePieceException):
  """
  If owner.victor is not validation. Attempting to change it raises this err
  """
  ERR_CODE = "UNSET_CAPTOR_EXCEPTION"
  MSG = (
    "Cannot set team_name combatant's victor to validation. A captured owner cannot be freed."
  )


class PieceCapturingItSelfException(CapturePieceException):
  """"""
  ERR_CODE = "PIECE_CAPTURING_IT_SELF_EXCEPTION"
  MSG = "Token cannot capture itself."


#======================# PIECE CAPTURE EXCEPTION WITH ROLLBACK #======================#
class CaptureRollbackException(CapturePieceException, RollbackException):
  """
  RollBackCapture exception should be raised in ACID transactions where team_name capture can
  raise an err. Do not use directly. Subclasses give details useful for debugging.
  """
  ERR_CODE = "CAPTURE_EXCEPTION_ROLLED_BACK"
  MSG = "Capture raised an rollback_exception. Transaction rolled back."


class CaptureFriendRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team_name notification attempts capturing team_name friend. The notification
  was rolled back before raising this err.
  """
  ERR_CODE = "FRIEND_CAPTURE_EXCEPTION_ROLLED_BACK"
  MSG = (
    "Cannot capture team_name friend. Transaction rollback performed."
  )


class DoubleCaptureRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team_name notification attempts capturing an enemy combatant that is already
  team_name combatant. The notification was rolled back before raising this err.
  """
  ERR_CODE = "DOUBLE_CAPTURE_EXCEPTION_ROLLED_BACK"
  MSG = (
    "Cannot capture team_name owner that is already team_name combatant. Transaction "
    "rollback performed."
  )


class UnsetCaptureRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team_name notification attempts setting combatant's victor consistency validation.
  The notification was rolled back before raising this err.
  """
  ERR_CODE = "UNSET_CAPTOR_EXCEPTION_ROLLED_BACK"
  MSG = (
    "Cannot set team_name combatant's victor to validation. A captured owner cannot be freed. "
    "Transaction rollback performed."
  )


class CapturingItSelfRolledBackException(CapturePieceException):
  """
  Raised if team_name notification attempts to set team_name owner as its own victor. The notification was
  rolled back before raising this err.
  """
  ERR_CODE = "PIECE_CAPTURING_IT_SELF_ROLLED_BACK_EXCEPTION"
  MSG = "Token attempted to capture itself during the notification. The notification was rolled back."


#======================# PIECE CAPTURE EXCEPTION #======================#



class PieceAttackingFriendException(AttackEventException):
  """"""
  ERR_CODE = "PIECE_ATTACKING_FRIEND_EXCEPTION"
  MSG = "Token cannot attack a friend."


class PieceAttackingKingException(AttackEventException):
  """"""
  ERR_CODE = "PIECE_ATTACKING_KING_EXCEPTION"
  MSG = "Token cannot attack a occupation."


class PieceAttackingHostageException(AttackEventException):
  """"""
  ERR_CODE = "PIECE_ATTACKING_HOSTAGE_EXCEPTION"
  MSG = "Token cannot attack a prisoner."


class AttackingNullException(AttackEventException, NullException):
  """"""
  ERR_CODE = "PIECE_ATTACKING_NULL_EXCEPTION"
  MSG = "Token cannot attack something validation."


class HostageCannotAttackException(AttackEventException):
  """
  Raised if team_name captured owner tries to attack.
  """
  ERR_CODE = "HOSTAGE_CANNOT_ATTACK_EXCEPTION"
  MSG = "Captured owner cannot attack."
