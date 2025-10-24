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
  'KingCheckMakingItSelfException',
  'AttackingFriendException',
  'AttackingEnemyKingException',
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
class NullAttackEventException(AttackEventException, NullException):
  """
  Raised if an entity, method, or operation requires team piece but gets null instead.
  Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
  Do not throw NullAttackException. Raise NullKingPiece or NullCombatantPiece instead.
  they are more descriptive and better suited for debugging.
  """
  ERROR_CODE = "NULL_ATTACK_ERROR"
  DEFAULT_MESSAGE = "Attack cannot be null"





class KingCaptureException(CapturePieceException):
  """
  Raised if team piece attempts to capture an enemy king. Kings can only be checked or
  checkmated.
  """
  ERROR_CODE = "KING_CAPTURE_ERROR"
  DEFAULT_MESSAGE = (
    "An enemy king cannot be captured. It can only be checked or checkmated."
  )
  
  class KingCaptureRolledBackExceptionCapture(CaptureRollbackException):
    """
    Raised if team notification attempts capturing an enemy. Kings can only be checked or
    checkmated. The notification was rolled back before raising this err.
    """
    ERROR_CODE = "KING_CAPTURE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
      "An enemy king cannot be captured. It can only be checked or checkmated. "
      "Transaction rollback performed."
    )


class AttackingEnemyKingException(AttackEventException):
  """"""
  ERROR_CODE = "ATTACKING_ENEMY_KING_ERROR"
  DEFAULT_MESSAGE = "An enemy cannot be attacked. They can only be checked or checkmated."


#======================# ATTACK_EVENT BUILD EXCEPTIONS #======================#
class AttackEventBuildFailedException(AttackEventException, BuildFailedException):
  """
  Indicates Coord could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "ATTACK_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "KingCheckEvent build failed."



