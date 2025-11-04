# chess/piece/travel/base/validator/traveler/exception.py

"""
Module: `chess.piece.travel.base.validator.traveler.exception`
Author: Banji Lawal
Created: 2025-10-06
Version: 1.0.1

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, validator, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected graph** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` graph.
It abstracts underlying Python exceptions into graph-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""

from chess.piece import TravelEventException
from chess.system import NullException, ValidationException, InconsistencyException

__all__ = [
  'TravelActorException',
  'TravelResourceException',

#====================== TravelEvent actor_candidate VALIDATION EXCEPTIONS #======================#
  'InvalidTravelActorException',
  'InvalidTravelResourceException',
  'NullTravelActorException',
  'NullTravelResourceException',
  'TravelActorNotFoundException',
  
  'NullTravelerEnvironmentTupleException',
  'NullDestinationEnvironmentTupleException',

# ====================== TRAVEL_ACTOR MOVE EXCEPTIONS #======================#
  'TravelActorMovingException',
  'NoInitialPlacementException',
  'ActorAlreadyAtDestinationException',
  'ActorNotOnRosterCannotMoveException',
  'RemovedBoardActorCannotMoveException',
  'CapturedActorCannotMoveException',

# ====================== TRAVEL_ACTOR SQUARE EXCEPTIONS #======================#
  'TravelActorSquareNotFoundException',
  'SquareMisMatchesTravelActorException'
]


class TravelActorException(TravelEventException):
  ERROR_CODE = "TRAVEL_ACTOR_ERROR"
  DEFAULT_MESSAGE = "An rollback_exception was raised by a TravelEvent traveler."


class TravelResourceException(TravelEventException):
  ERROR_CODE = "TRAVEL_RESOURCE_ERROR"
  DEFAULT_MESSAGE = "An rollback_exception was raised by a TravelEvent resource."

#====================== TRAVEL ACTOR VALIDATION EXCEPTIONS #======================#
class NullTravelActorException(TravelActorException, NullException):
  ERROR_CODE = "NULL_TRAVEL_ACTOR_ERROR"
  DEFAULT_MESSAGE = "A TravelEvent traveler cannot be null."

class NullTravelResourceException(TravelResourceException, NullException):
  ERROR_CODE = "NULL_TRAVEL_RESOURCE_ERROR"
  DEFAULT_MESSAGE = "A TravelEvent resource cannot be null."

class NullTravelerEnvironmentTupleException(TravelActorException, NullException):
  ERROR_CODE = "NULL_TRAVELER_ENVIRONMENT_TUPLE_ERROR"
  DEFAULT_MESSAGE = "Piece-Board-Tuple passed to BoardActorValidator cannot be null."
  
class NullDestinationEnvironmentTupleException(TravelResourceException, NullException):
  ERROR_CODE = "NULL_DESTINATION__ENVIRONMENT_TUPLE_ERROR"
  DEFAULT_MESSAGE = "Square-Board-Tuple passed to TravelResourceValidator cannot be null."

class InvalidTravelActorException(TravelActorException, ValidationException):
  ERROR_CODE = "TRAVEL_ACTOR_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Validation of a TravelEvent traveler failed."

class InvalidTravelResourceException(TravelResourceException, ValidationException):
  ERROR_CODE = "TRAVEL_RESOURCE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Validation of a TravelEvent resource failed."

class TravelActorNotFoundException(TravelActorException, InconsistencyException):
  ERROR_CODE = "TRAVEL_ACTOR_NOT_FOUND_ERROR"
  DEFAULT_MESSAGE = (
    "TravelEvent actor_candidate was not found during the board search. There may be a service inconsistency."
  )

# ====================== TRAVEL_ACTOR MOVE EXCEPTIONS #======================#
class TravelActorMovingException(TravelActorException):
  ERROR_CODE = "TRAVEL_ACTOR_MOVE_ERROR"
  DEFAULT_MESSAGE = "TravelEvent actor_candidate raised a moving violation. Candidate cannot travel."

class NoInitialPlacementException(TravelActorMovingException):
  """"""
  ERROR_CODE = "ACTOR_DID_NOT_HAVE_INITIAL_PLACEMENT_ERROR"
  DEFAULT_MESSAGE = (
    "TravelEvent actor_candidate did not have an initial placement on the board. Its position history is empty. "
    "Candidate cannot travel."
  )

class ActorAlreadyAtDestinationException(TravelActorMovingException):
  """"""
  ERROR_CODE = "ACTOR_ALREADY_AT_DESTINATION_ERROR"
  DEFAULT_MESSAGE = "TravelEvent actor_candidate is already at the destination square. There is nn need to travel."

class ActorNotOnRosterCannotMoveException(TravelActorMovingException):
  """"""
  ERROR_CODE = "ACTOR_NOT_ON_ROSTER_MOVE_ERROR"
  DEFAULT_MESSAGE = "TravelEvent actor_candidate is not on their team's roster. Candidate cannot travel."

class RemovedBoardActorCannotMoveException(TravelActorMovingException):
  """"""
  ERROR_CODE = "ACTOR_NOT_ON_BOARD_MOVE_ERROR"
  DEFAULT_MESSAGE = (
    "TravelEvent actor_candidate is not on the board. Candidate cannot travel."
  )

class CapturedActorCannotMoveException(TravelActorMovingException):
  """"""
  ERROR_CODE = "CAPTURED_ACTOR_MOVE_ERROR"
  DEFAULT_MESSAGE = (
    "TravelEvent actor_candidate has been captured by the enemy. Captured pieces are not on the board."
    "Candidate cannot travel."
  )

class CheckMatedKingCannotMoveException(TravelActorMovingException):
  """"""
  ERROR_CODE = "CHECK_MATED_KING_MOVE_ERROR"
  DEFAULT_MESSAGE = (
    "The occupation is checkmated. When a occupation is checkmated the game ends. If you are seeing this message "
    "the win has not been processed correctly."
  )


# ====================== TRAVEL_ACTOR SQUARE EXCEPTIONS #======================#
class TravelActorSquareNotFoundException(TravelActorException, InconsistencyException):
  """"""
  ERROR_CODE = "TRAVEL_ACTOR_SQUARE_NOT_FOUND_ERROR"
  DEFAULT_MESSAGE = (
    "BoardSearch did not find a square associated with the actor_candidate's coord. There may be a service "
    "inconsistency."
  )

class SquareMisMatchesTravelActorException(TravelActorException, InconsistencyException):
  """"""
  ERROR_CODE = "SQUARE_MISMATCHES_TRAVEL_ACTOR_ERROR"
  DEFAULT_MESSAGE = "The square does not contain the actor_candidate. There may be a service inconsistency."
