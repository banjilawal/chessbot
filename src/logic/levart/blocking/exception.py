# src/logic/owner/travel/blocking/rollback_exception.py

"""
Module: `logic.owner.travel.blocking.rollback_exception`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from logic.piece import TravelEventException

"""
Module: logic.system.travel.rollback_exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` integrity requirement.
  2. A satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module's only covers exception raised by `IdValidator`;

# SECTION 3: Limitations
  1. Does not provide logic for fixing the errors or causing the rollback_exception being raised.
       `IdValidator` is responsible for the logic which raises these exception.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. Discoverability.
  3. Encapsulations.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.


# SECTION 6 - Feature Delivery Mechanism:
1. Exception specific to verifying ids.

# SECTION 7 - Dependencies:
* From `logic.system`:
    `ChessException`, `ContextException`, `ResultException`

# SECTION 8 - Contains:
See the list of exception in the `__all__` list following (e.g., `EventException`,`TransactionException`).
"""


from logic.system import ChessException, NullException, BuildException, ValidationException

__all__ = [
  'BlockingEventException',

#======================# BLOCKING_EVENT VALIDATION EXCEPTION #======================#
  'NullBlockingEventException',
  'ActorBlockingOwnSquareException',
  'ActorSameAsBlockerException',
  'EnemyCannotBeBlockerException',
  'DiscoveryAlreadyExistsException'
]


class BlockingEventException(TravelEventException):
  """"""
  ERR_CODE = "BLOCKING_EVENT_EXCEPTION"
  MSG = "BlockingEvent raised an exception."

#======================# BLOCKING_EVENT VALIDATION EXCEPTION #======================#
class InvalidBlockingEventException(TravelEventException, ValidationException):
  """"""
  ERR_CODE = "BLOCKING_EVENT_EXCEPTION"
  MSG = "BlockingEvent raised an exception."
  
class NullBlockingEventException(BlockingEventException, NullException):
  """"""
  ERR_CODE = "NULL_BLOCKING_EVENT_EXCEPTION"
  MSG = "BlockingEvent cannot be validation"

class ActorBlockingOwnSquareException(BlockingEventException):
  """"""
  ERR_CODE = "ACTOR_BLOCKING_OWN_SQUARE_EXCEPTION"
  MSG = "Actor cannot block itself from its own square_name"

class ActorSameAsBlockerException(BlockingEventException):
  """"""
  ERR_CODE = "ACTOR_SAME_AS_BLOCKING_FRIEND_EXCEPTION"
  MSG = "Actor and their blocking friend cannot be the same."

class EnemyCannotBeBlockerException(BlockingEventException):
  """"""
  ERR_CODE = "BLOCKER_IS_ENEMY_EXCEPTION"
  MSG = ("Blocker cannot be an enemy. An enemy at the destination is attacked or checked."
     " Only friends can block the owner."
  )


class DiscoveryAlreadyExistsException(BlockingEventException):
  """"""
  ERR_CODE = "DISCOVERY_ALREADY_EXISTS_EXCEPTION"
  MSG = "The Discovery already exists in the dataset."

#
# class DoubleEncounterException(BlockingEventException):
#   """"""
#   ERR_CODE = "DOUBLE_BLOCKING_EXCEPTION"
#   MSG = "The friend has already been encountered."
#
# class InvalidEncounterException(BlockingEventException, ValidationException):
#   """"""
#   ERR_CODE = "INVALID_BLOCKING_EVENT_EXCEPTION"
#   MSG = "BlockingEventException validation failed."
#
#
# #======================# BLOCKING_EVENT BUILD EXCEPTION #======================#
# class BlockingEventExceptionBuildException(BlockingEventException, BuildException):
#   """
#   Indicate That  Coord could not be built. Wraps and re-raises errors that occurred
#   during builder.
#   """
#   ERR_CODE = "BLOCKING_EVENT_BUILD_FAILED"
#   MSG = "BlockingEventException build failed."
#
#
# # src/logic.point.rollback_exception.py
#
# """
# Module: logic.point.rollback_exception
# Author: Banji Lawal
# Created: 2025-10-04
# version: 1.0.0
#
# SCOPE:
# -----
# This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
# creation, coord_stack_validator, and manipulation of **Coord objects**. It handles boundary checks (row/column)
# limits and validation checks. It does not contain any logic for *raising* these exception; that responsibility
# falls to the `CoordValidator` and `CoordBuilder`processes.
#
# THEME:
# -----
# **Comprehensive Domain Error Persona.** The central theme is to provide team_name
# highly granular and hierarchical set of exception, ensuring that callers can
# catch and handle errors based on both the **type of failure** (e.g., `NullException`)
# and the **affected graph** (e.g., `CoordException`). This enables precise error
# logging and handling throughout the system.
#
# PURPOSE:
# -------
# To serve as the **centralized error dictionary** for the `Coord` graph.
# It abstracts underlying Python exception into graph-specific, custom error types
# to improve code clarity and facilitate robust error handling within the chess engine.
#
# DEPENDENCIES:
# ------------
# Requires base rollback_exception classes and constants from the core system:
# From `logic.system`:
#   * Constants: `NUMBER_OF_ROWS`, `NUMBER_OF_COLUMNS`
#   * Exception: `ChessException`, `ValidationException`, `NullException`,
#         `BuildException`.
#
# CONTAINS:
# --------
# See the list of exception in the `__all__` list following (e.g., `CoordException`,
# `NullCoordException`, `RowAboveBoundsException`).
# """
#
# from logic.owner import TravelEventException
# from logic.system import NullException, ValidationException, InconsistencyException
#
# __all__ = [
#   'TravelActorException',
#
#   #====================== TravelEvent actor_candidate VALIDATION EXCEPTION #======================#
#   'InvalidTravelActorException',
#   'NullTravelActorException',
#   'TravelActorNotFoundException',
#
#   #====================== TRAVEL_ACTOR MOVE EXCEPTION #======================#
#   'TravelActorMovingException',
#   'NoInitialPlacementException',
#   'ActorAlreadyAtDestinationException',
#   'DisabledUnRosteredPieceCannotActException',
#   'BoardPieceRemovedCannotActException',
#   'CapturedActorCannotMoveException',
#
#   #====================== TRAVEL_ACTOR SQUARE EXCEPTION #======================#
#   'PieceSquareNotFoundException',
#   'SquareMisMatchesPieceException'
# ]
#
#
# class TravelActorException(TravelEventException):
#   ERR_CODE = "TRAVEL_ACTOR_EXCEPTION"
#   MSG = "TravelEvent actor_candidate actor_candidate raised an exception."
#
#
# #====================== TRAVEL ACTOR VALIDATION EXCEPTION #======================#
# class NullTravelActorException(TravelActorException, NullException):
#   ERR_CODE = "NULL_TRAVEL_ACTOR_EXCEPTION"
#   MSG = "TravelEvent actor_candidate cannot be null."
#
#
# class InvalidTravelActorException(TravelActorException, ValidationException):
#   ERR_CODE = "TRAVEL_ACTOR_VALIDATION_EXCEPTION"
#   MSG = "TravelEvent actor_candidate validation failed."
#
#
# class TravelActorNotFoundException(TravelActorException, InconsistencyException):
#   ERR_CODE = "TRAVEL_ACTOR_NOT_FOUND_EXCEPTION"
#   MSG = (
#     "TravelEvent actor_candidate was not found during the board searcher. There may be a entity_service inconsistency."
#   )
#
#
# #====================== TRAVEL_ACTOR MOVE EXCEPTION #======================#
# class TravelActorMovingException(TravelActorException):
#   ERR_CODE = "TRAVEL_ACTOR_MOVE_EXCEPTION"
#   MSG = "TravelEvent actor_candidate raised a moving violation. Candidate cannot travel."
#
#
# class NoInitialPlacementException(TravelActorMovingException):
#   """"""
#   ERR_CODE = "ACTOR_DID_NOT_HAVE_INITIAL_PLACEMENT_EXCEPTION"
#   MSG = (
#     "TravelEvent actor_candidate did not have an initial placement on the board. Its position history is empty. "
#     "Candidate cannot travel."
#   )
#
#
# class ActorAlreadyAtDestinationException(TravelActorMovingException):
#   """"""
#   ERR_CODE = "ACTOR_ALREADY_AT_DESTINATION_EXCEPTION"
#   MSG = "TravelEvent actor_candidate is already at the destination square_name. There is nn need to travel."
#
#
# class DisabledUnRosteredPieceCannotActException(TravelActorMovingException):
#   """"""
#   ERR_CODE = "ACTOR_NOT_ON_ROSTER_MOVE_EXCEPTION"
#   MSG = "TravelEvent actor_candidate is not on their team_name's roster. Candidate cannot travel."
#
#
# class BoardPieceRemovedCannotActException(TravelActorMovingException):
#   """"""
#   ERR_CODE = "ACTOR_NOT_ON_BOARD_MOVE_EXCEPTION"
#   MSG = (
#     "TravelEvent actor_candidate is not on the board. Candidate cannot travel."
#   )
#
#
# class CapturedActorCannotMoveException(TravelActorMovingException):
#   """"""
#   ERR_CODE = "CAPTURED_ACTOR_MOVE_EXCEPTION"
#   MSG = (
#     "TravelEvent actor_candidate has been captured by the enemy. Captured pieces are not on the board."
#     "Candidate cannot travel."
#   )
#
#
# class CheckmatedKingCannotActException(TravelActorMovingException):
#   """"""
#   ERR_CODE = "CHECK_MATED_KING_MOVE_EXCEPTION"
#   MSG = (
#     "The occupation is checkmated. When a occupation is checkmated the game ends. If you are seeing this msg "
#     "the win has not been processed correctly."
#   )
#
#
# #====================== TRAVEL_ACTOR SQUARE EXCEPTION #======================#
# class PieceSquareNotFoundException(TravelActorException, InconsistencyException):
#   """"""
#   ERR_CODE = "TRAVEL_ACTOR_SQUARE_NOT_FOUND_EXCEPTION"
#   MSG = (
#     "BoardSearch did not find a square_name associated with the actor_candidate's point. There may be a entity_service "
#     "inconsistency."
#   )
#
#
# class SquareMisMatchesPieceException(TravelActorException, InconsistencyException):
#   """"""
#   ERR_CODE = "SQUARE_MISMATCHES_TRAVEL_ACTOR_EXCEPTION"
#   MSG = "The square_name does not contain the actor_candidate. There may be a entity_service inconsistency."
#
#
#
#
#
