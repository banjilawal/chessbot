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
#====================== KING_OCCUPATION_EVENT EXCEPTION #======================#
  'KingOccupationEventException',
  
#====================== KING_OCCUPATION_EVENT VALIDATION EXCEPTION #======================#
  'NullKingOccupationEventException',
  'InvalidKingOccupationEventException',
  'OccupationDestinationNotEmptyException',
]

#====================== KING_OCCUPATION_EVENT EXCEPTION #======================#
class KingOccupationEventException(TravelEventException):
  """
  A base class for all exception related to the KingOccupationEvent. Do not use directly. Subclasses provide
  fine-grained msgs and error codes better for debugging and logging.
  """
  DEFAULT_CODE = "KING_OCCUPATION_EVENT_ERROR"
  MSG = "An KingOccupationEvent raised an exception."


#====================== KING_OCCUPATION_EVENT VALIDATION EXCEPTION #======================#
class NullKingOccupationEventException(KingOccupationEventException, NullException):
  """Raised by methods, entities, and models that require KingOccupationEvent but receive validation instead."""
  ERR_CODE = "NULL_KING_OCCUPATION_EVENT_ERROR"
  MSG = "An KingOccupationEvent cannot be null."


class InvalidKingOccupationEventException(KingOccupationEventException, ValidationException):
  """Raised by KingOccupationEventValidators if a candidate fails coord_stack_validator."""
  ERR_CODE = "KING_OCCUPATION_EVENT_VALIDATION_ERROR"
  MSG = "KingOccupationEvent validation failed."


class OccupationDestinationNotEmptyException(KingOccupationEventException):
  """Raised by KingOccupationEventValidators if a candidate fails coord_stack_validator."""
  ERR_CODE = "KING_OCCUPATION_EVENT_DESTINATION_NOT_EMPTY_ERROR"
  MSG = "KingOccupationEvent destination square_name is not empty."
  
#=== ATTACK_EVENT BUILD EXCEPTION #======================#
class AttackEventBuilderException(AttackEventException, BuilderException):
  """
  Indicate That  Coord could not be built. Wraps and re-raises errors that occurred
  during builder.
  """
  ERR_CODE = "ATTACK_EVENT_BUILD_FAILED"
  MSG = "AttackEventBuilder failed to create kingOccupationEvent"


#=== ATTACK_EVENT BUILD EXCEPTION #======================#
class UnexpectedNullEnemyException(AttackEventException):
  DEFAULT_CODE = "UNEXPECTED_NULL_ENEMY"
  MSG = "Target actor_candidate is unexpectedly validation during capture; this should not happen."




#
# --- Rollback Attack Errors (Dual Inheritance) ---
class SetCaptorRolledBackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SET_CAPTOR_ERROR_ROLLED_BACK"
  MSG = "Setting victor failed. Transaction rolled back performed."


class EmptyDestinationSquareRolledBackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SET_CAPTOR_ERROR_ROLLED_BACK"
  MSG = "Setting victor failed. Transaction rolled back performed."


class RosterRemovalRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "ROSTER_REMOVAL_ROLLBACK"
  MSG = "Failed to remove actor_candidate from enemy roster after assigning victor; rollback performed."


class HostageAdditionRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "HOSTAGE_ADDITION_ROLLBACK"
  MSG = "Failed to add captured actor_candidate to victor's prisoner list; rollback performed."


class BoardPieceRemovalRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "BOARD_REMOVAL_ROLLBACK"
  MSG = "Failed to remove captured actor_candidate from board_validator; rollback performed."


class SquareOccupationRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SQUARE_OCCUPATION_ROLLBACK"
  MSG = "Failed to occupation target square_name after capture; rollback executed."


class SourceSquareRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SOURCE_SQUARE_ROLLBACK"
  MSG = "Failed to clear attacker's source square_name; rollback executed."


class PositionUpdateRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "POSITION_UPDATE_ROLLBACK"
  MSG = "Failed to update actor_candidate's position history after move; rollback executed."


#======================# ATTACKING PIECE EXCEPTION #======================#
