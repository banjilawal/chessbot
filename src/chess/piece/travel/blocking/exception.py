# src/chess/piece/travel/blocking/rollback_exception.py

"""
Module: `chess.piece.travel.blocking.rollback_exception`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from chess.piece import TravelEventException

"""
Module: chess.system.travel.rollback_exception
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
  1. Does not provide logic for fixing the errors or causing the rollback_exception being raised.
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


from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
  'BlockingEventException',

# ======================# BLOCKING_EVENT VALIDATION EXCEPTIONS #======================#
  'NullBlockingEventException',
  'ActorBlockingOwnSquareException',
  'ActorSameAsBlockerException',
  'EnemyCannotBeBlockerException',
  'DiscoveryAlreadyExistsException'
]


class BlockingEventException(TravelEventException):
  """"""
  ERROR_CODE = "BLOCKING_EVENT_ERROR"
  DEFAULT_MESSAGE = "BlockingEvent raised an rollback_exception."

#======================# BLOCKING_EVENT VALIDATION EXCEPTIONS #======================#
class InvalidBlockingEventException(TravelEventException, ValidationException):
  """"""
  ERROR_CODE = "BLOCKING_EVENT_ERROR"
  DEFAULT_MESSAGE = "BlockingEvent raised an rollback_exception."
  
class NullBlockingEventException(BlockingEventException, NullException):
  """"""
  ERROR_CODE = "NULL_BLOCKING_EVENT_ERROR"
  DEFAULT_MESSAGE = "BlockingEvent cannot be null"

class ActorBlockingOwnSquareException(BlockingEventException):
  """"""
  ERROR_CODE = "ACTOR_BLOCKING_OWN_SQUARE_ERROR"
  DEFAULT_MESSAGE = "Actor cannot block itself from its own square"

class ActorSameAsBlockerException(BlockingEventException):
  """"""
  ERROR_CODE = "ACTOR_SAME_AS_BLOCKING_FRIEND_ERROR"
  DEFAULT_MESSAGE = "Actor and their blocking friend cannot be the same."

class EnemyCannotBeBlockerException(BlockingEventException):
  """"""
  ERROR_CODE = "BLOCKER_IS_ENEMY_ERROR"
  DEFAULT_MESSAGE = ("Blocker cannot be an enemy. An enemy at the destination is attacked or checked."
     " Only friends can block the agent."
  )


class DiscoveryAlreadyExistsException(BlockingEventException):
  """"""
  ERROR_CODE = "DISCOVERY_ALREADY_EXISTS_ERROR"
  DEFAULT_MESSAGE = "The Discovery already exists in the collection."

#
# class DoubleEncounterException(BlockingEventException):
#   """"""
#   ERROR_CODE = "DOUBLE_BLOCKING_ERROR"
#   DEFAULT_MESSAGE = "The friend has already been encountered."
#
# class InvalidEncounterException(BlockingEventException, ValidationException):
#   """"""
#   ERROR_CODE = "INVALID_BLOCKING_EVENT_ERROR"
#   DEFAULT_MESSAGE = "BlockingEventException validator failed."
#
#
# #======================# BLOCKING_EVENT BUILD EXCEPTIONS #======================#
# class BlockingEventExceptionBuildFailedException(BlockingEventException, BuildFailedException):
#   """
#   Indicates Coord could not be built. Wraps and re-raises errors that occurred
#   during build.
#   """
#   ERROR_CODE = "BLOCKING_EVENT_BUILD_FAILED_ERROR"
#   DEFAULT_MESSAGE = "BlockingEventException build failed."
#
#
# # src/chess.coord.rollback_exception.py
#
# """
# Module: chess.coord.rollback_exception
# Author: Banji Lawal
# Created: 2025-10-04
# version: 1.0.0
#
# SCOPE:
# -----
# This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
# creation, validator, and manipulation of **Coord objects**. It handles boundary checks (row/column)
# limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
# falls to the `CoordValidator` and `CoordBuilder`processes.
#
# THEME:
# -----
# **Comprehensive Domain Error Catalog.** The central theme is to provide team
# highly granular and hierarchical set of exceptions, ensuring that callers can
# catch and handle errors based on both the **type of failure** (e.g., `NullException`)
# and the **affected domain** (e.g., `CoordException`). This enables precise error
# logging and handling throughout the system.
#
# PURPOSE:
# -------
# To serve as the **centralized error dictionary** for the `Coord` domain.
# It abstracts underlying Python exceptions into domain-specific, custom error types
# to improve code clarity and facilitate robust error handling within the chess engine.
#
# DEPENDENCIES:
# ------------
# Requires base rollback_exception classes and constants from the core system:
# From `chess.system`:
#   * Constants: `ROW_SIZE`, `COLUMN_SIZE`
#   * Exceptions: `ChessException`, `ValidationException`, `NullException`,
#         `BuildFailedException`.
#
# CONTAINS:
# --------
# See the list of exceptions in the `__all__` list following (e.g., `CoordException`,
# `NullCoordException`, `RowAboveBoundsException`).
# """
#
# from chess.piece import TravelEventException
# from chess.system import NullException, ValidationException, InconsistencyException
#
# __all__ = [
#   'TravelActorException',
#
#   # ====================== TravelEvent actor_candidate VALIDATION EXCEPTIONS #======================#
#   'InvalidTravelActorException',
#   'NullTravelActorException',
#   'TravelActorNotFoundException',
#
#   # ====================== TRAVEL_ACTOR MOVE EXCEPTIONS #======================#
#   'TravelActorMovingException',
#   'NoInitialPlacementException',
#   'ActorAlreadyAtDestinationException',
#   'ActorNotOnRosterCannotMoveException',
#   'ActorNotOnBoardCannotMoveException',
#   'CapturedActorCannotMoveException',
#
#   # ====================== TRAVEL_ACTOR SQUARE EXCEPTIONS #======================#
#   'PieceSquareNotFoundException',
#   'SquareMisMatchesPieceException'
# ]
#
#
# class TravelActorException(TravelEventException):
#   ERROR_CODE = "TRAVEL_ACTOR_ERROR"
#   DEFAULT_MESSAGE = "TravelEvent actor_candidate actor_candidate raised an rollback_exception."
#
#
# # ====================== TRAVEL ACTOR VALIDATION EXCEPTIONS #======================#
# class NullTravelActorException(TravelActorException, NullException):
#   ERROR_CODE = "NULL_TRAVEL_ACTOR_ERROR"
#   DEFAULT_MESSAGE = "TravelEvent actor_candidate cannot be null."
#
#
# class InvalidTravelActorException(TravelActorException, ValidationException):
#   ERROR_CODE = "TRAVEL_ACTOR_VALIDATION_ERROR"
#   DEFAULT_MESSAGE = "TravelEvent actor_candidate validator failed."
#
#
# class TravelActorNotFoundException(TravelActorException, InconsistencyException):
#   ERROR_CODE = "TRAVEL_ACTOR_NOT_FOUND_ERROR"
#   DEFAULT_MESSAGE = (
#     "TravelEvent actor_candidate was not found during the board search. There may be a data inconsistency."
#   )
#
#
# # ====================== TRAVEL_ACTOR MOVE EXCEPTIONS #======================#
# class TravelActorMovingException(TravelActorException):
#   ERROR_CODE = "TRAVEL_ACTOR_MOVE_ERROR"
#   DEFAULT_MESSAGE = "TravelEvent actor_candidate raised a moving violation. Candidate cannot travel."
#
#
# class NoInitialPlacementException(TravelActorMovingException):
#   """"""
#   ERROR_CODE = "ACTOR_DID_NOT_HAVE_INITIAL_PLACEMENT_ERROR"
#   DEFAULT_MESSAGE = (
#     "TravelEvent actor_candidate did not have an initial placement on the board. Its position history is empty. "
#     "Candidate cannot travel."
#   )
#
#
# class ActorAlreadyAtDestinationException(TravelActorMovingException):
#   """"""
#   ERROR_CODE = "ACTOR_ALREADY_AT_DESTINATION_ERROR"
#   DEFAULT_MESSAGE = "TravelEvent actor_candidate is already at the destination square. There is nn need to travel."
#
#
# class ActorNotOnRosterCannotMoveException(TravelActorMovingException):
#   """"""
#   ERROR_CODE = "ACTOR_NOT_ON_ROSTER_MOVE_ERROR"
#   DEFAULT_MESSAGE = "TravelEvent actor_candidate is not on their team's roster. Candidate cannot travel."
#
#
# class ActorNotOnBoardCannotMoveException(TravelActorMovingException):
#   """"""
#   ERROR_CODE = "ACTOR_NOT_ON_BOARD_MOVE_ERROR"
#   DEFAULT_MESSAGE = (
#     "TravelEvent actor_candidate is not on the board. Candidate cannot travel."
#   )
#
#
# class CapturedActorCannotMoveException(TravelActorMovingException):
#   """"""
#   ERROR_CODE = "CAPTURED_ACTOR_MOVE_ERROR"
#   DEFAULT_MESSAGE = (
#     "TravelEvent actor_candidate has been captured by the enemy. Captured pieces are not on the board."
#     "Candidate cannot travel."
#   )
#
#
# class CheckMatedKingCannotMoveException(TravelActorMovingException):
#   """"""
#   ERROR_CODE = "CHECK_MATED_KING_MOVE_ERROR"
#   DEFAULT_MESSAGE = (
#     "The king is checkmated. When a king is checkmated the game ends. If you are seeing this message "
#     "the win has not been processed correctly."
#   )
#
#
# # ====================== TRAVEL_ACTOR SQUARE EXCEPTIONS #======================#
# class PieceSquareNotFoundException(TravelActorException, InconsistencyException):
#   """"""
#   ERROR_CODE = "TRAVEL_ACTOR_SQUARE_NOT_FOUND_ERROR"
#   DEFAULT_MESSAGE = (
#     "BoardSearch did not find a square associated with the actor_candidate's coord. There may be a data "
#     "inconsistency."
#   )
#
#
# class SquareMisMatchesPieceException(TravelActorException, InconsistencyException):
#   """"""
#   ERROR_CODE = "SQUARE_MISMATCHES_TRAVEL_ACTOR_ERROR"
#   DEFAULT_MESSAGE = "The square does not contain the actor_candidate. There may be a data inconsistency."
#
#
#
#
#
