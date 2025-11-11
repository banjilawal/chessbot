# src/chess/owner/travel/occupation/rollback_exception.py

"""
Module: `chess.owner.travel.occupation.rollback_exception`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.piece import TravelEventException
from chess.system import NullException, ValidationException

__all__ = [
#====================== KING_OCCUPATION_EVENT EXCEPTIONS #======================#
  'KingOccupationEventException',
  
#====================== KING_OCCUPATION_EVENT VALIDATION EXCEPTIONS #======================#
  'NullKingOccupationEventException',
  'InvalidKingOccupationEventException',
  'OccupationDestinationNotEmptyException',
]

#====================== KING_OCCUPATION_EVENT EXCEPTIONS #======================#
class KingOccupationEventException(TravelEventException):
  """
  A base class for all exceptions related to the KingOccupationEvent. Do not use directly. Subclasses provide
  fine-grained messages and error codes better for debugging and logging.
  """
  DEFAULT_CODE = "KING_OCCUPATION_EVENT_ERROR"
  DEFAULT_MESSAGE = "An KingOccupationEvent raised an rollback_exception."


#====================== KING_OCCUPATION_EVENT VALIDATION EXCEPTIONS #======================#
class NullKingOccupationEventException(KingOccupationEventException, NullException):
  """Raised by methods, entities, and models that require KingOccupationEvent but receive null instead."""
  ERROR_CODE = "NULL_KING_OCCUPATION_EVENT_ERROR"
  DEFAULT_MESSAGE = "An KingOccupationEvent cannot be null."


class InvalidKingOccupationEventException(KingOccupationEventException, ValidationException):
  """Raised by KingOccupationEventValidators if a candidate fails validator."""
  ERROR_CODE = "KING_OCCUPATION_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "KingOccupationEvent validation failed."


class OccupationDestinationNotEmptyException(KingOccupationEventException):
  """Raised by KingOccupationEventValidators if a candidate fails validator."""
  ERROR_CODE = "KING_OCCUPATION_EVENT_DESTINATION_NOT_EMPTY_ERROR"
  DEFAULT_MESSAGE = "KingOccupationEvent destination square is not empty."
  
#=== ATTACK_EVENT BUILD EXCEPTIONS #======================#
class AttackEventBuilderException(AttackEventException, BuilderException):
  """
  Indicates Coord could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "ATTACK_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "AttackEventBuilder failed to create kingOccupationEvent"


#=== ATTACK_EVENT BUILD EXCEPTIONS #======================#
class UnexpectedNullEnemyException(AttackEventException):
  DEFAULT_CODE = "UNEXPECTED_NULL_ENEMY"
  DEFAULT_MESSAGE = "Target actor_candidate is unexpectedly null during capture; this should not happen."




#
# --- Rollback Attack Errors (Dual Inheritance) ---
class SetCaptorRolledBackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SET_CAPTOR_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Setting captor failed. Transaction rolled back performed."


class EmptyDestinationSquareRolledBackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SET_CAPTOR_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Setting captor failed. Transaction rolled back performed."


class RosterRemovalRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "ROSTER_REMOVAL_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to remove actor_candidate from enemy roster after assigning captor; rollback performed."


class HostageAdditionRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "HOSTAGE_ADDITION_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to add captured actor_candidate to captor's hostage list; rollback performed."


class BoardPieceRemovalRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "BOARD_REMOVAL_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to remove captured actor_candidate from board_validator; rollback performed."


class SquareOccupationRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SQUARE_OCCUPATION_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to occupation target square after capture; rollback executed."


class SourceSquareRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SOURCE_SQUARE_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to clear attacker's source square; rollback executed."


class PositionUpdateRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "POSITION_UPDATE_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to update actor_candidate's position history after move; rollback executed."


# ======================# ATTACKING PIECE EXCEPTIONS #======================#
class HostageActivityException(PieceException):
  """
  Several exceptions can be raised during capture operations. This class is the parent of
  exceptions an attacking owner can raised. Do not use directly. Subclasses give details
  useful for debugging.
  """
  ERROR_CODE = "HOSTAGE_ACTIVITY_ERROR"
  DEFAULT_MESSAGE = "Hostage owner cannot move, blocking, or attack."


class HostageCannotAttackException(HostageActivityException):
  """
  Raised if team_name captured owner tries to attack.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_ATTACK_ERROR"
  DEFAULT_MESSAGE = "Captured owner cannot attack."


class HostageCannotMoveException(HostageActivityException):
  """
  Raised if team_name captured owner tries to move.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_MOVE_ERROR"
  DEFAULT_MESSAGE = "Captured owner cannot move."


class HostageCannotScanException(HostageActivityException):
  """
  Raised if team_name captured owner tries to blocking team_name square.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_SCAN_ERROR"
  DEFAULT_MESSAGE = "Captured owner cannot blocking team_name sqaure."


