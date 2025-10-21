# src/chess/piece/event/attack/event/travel_exception.py

"""
Module: chess.piece.event.attack.event.exception
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
  'DoublyAttackingPrisonerException',
]


class AttackEventException(ChessException):
  """
  Super class of all exceptions team Piece object raises. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching
  all piece exceptions
  """
  ERROR_CODE = "ATTACK_ERROR"
  DEFAULT_MESSAGE = "An attack raised an exception."


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


#======================# ATTACK_EVENT BUILD EXCEPTIONS #======================#
class AttackEventBuildFailedException(AttackEventException, BuildFailedException):
  """
  Indicates Coord could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "ATTACK_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "CheckEvent build failed."