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
#====================== OCCUPATION_EVENT EXCEPTION #======================#
  'OccupationEventException',
  
#====================== OCCUPATION_EVENT VALIDATION EXCEPTION #======================#
  'NullOccupationEventException',
  'InvalidOccupationEventException',
  'OccupationDestinationNotEmptyException',
]

#====================== OCCUPATION_EVENT EXCEPTION #======================#
class OccupationEventException(TravelEventException):
  """
  A base class for all exception related to the OccupationEvent. Do not use directly. Subclasses provide
  fine-grained messages and error codes better for debugging and logging.
  """
  DEFAULT_CODE = "OCCUPATION_EVENT_ERROR"
  DEFAULT_MESSAGE = "An OccupationEvent raised an exception."


#====================== OCCUPATION_EVENT VALIDATION EXCEPTION #======================#
class NullOccupationEventException(OccupationEventException, NullException):
  """Raised by methods, entities, and models that require OccupationEvent but receive validation instead."""
  ERROR_CODE = "NULL_OCCUPATION_EVENT_ERROR"
  DEFAULT_MESSAGE = "An OccupationEvent cannot be null."


class InvalidOccupationEventException(OccupationEventException, ValidationException):
  """Raised by OccupationEventValidators if a candidate fails coord_stack_validator."""
  ERROR_CODE = "OCCUPATION_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "OccupationEvent validation failed."


class OccupationDestinationNotEmptyException(OccupationEventException):
  """Raised by OccupationEventValidators if a candidate fails coord_stack_validator."""
  ERROR_CODE = "OCCUPATION_EVENT_DESTINATION_NOT_EMPTY_ERROR"
  DEFAULT_MESSAGE = "OccupationEvent destination square_name is not empty."
  
#=== ATTACK_EVENT BUILD EXCEPTION #======================#
class AttackEventBuilderException(AttackEventException, BuilderException):
  """
  Indicate That  Coord could not be built. Wraps and re-raises errors that occurred
  during builder.
  """
  ERROR_CODE = "ATTACK_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "AttackEventBuilder failed to create occupationEvent"


#=== ATTACK_EVENT BUILD EXCEPTION #======================#
class UnexpectedNullEnemyException(AttackEventException):
  DEFAULT_CODE = "UNEXPECTED_NULL_ENEMY"
  DEFAULT_MESSAGE = "Target actor_candidate is unexpectedly validation during capture; this should not happen."




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
  DEFAULT_MESSAGE = "Failed to occupation target square_name after capture; rollback executed."


class SourceSquareRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "SOURCE_SQUARE_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to clear attacker's source square_name; rollback executed."


class PositionUpdateRollbackException(AttackEventException, RollbackException):
  DEFAULT_CODE = "POSITION_UPDATE_ROLLBACK"
  DEFAULT_MESSAGE = "Failed to update actor_candidate's position history after move; rollback executed."


#======================# ATTACKING PIECE EXCEPTION #======================#
class HostageActivityException(PieceException):
  """
  Several exception can be raised during capture rollback. This class is the parent of
  exception an attacking owner can raised. Do not use directly. Subclasses give details
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
  Raised if team_name captured owner tries to blocking team_name square_name.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_SCAN_ERROR"
  DEFAULT_MESSAGE = "Captured owner cannot blocking team_name sqaure."


