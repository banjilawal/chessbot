# src/chess.coord.travel_exception.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected domain** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` domain.
It abstracts underlying Python exceptions into domain-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
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

#====================== TravelEvent actor_candidate VALIDATION EXCEPTIONS #======================#
  'InvalidTravelActorException',
  'NullTravelActorException',
  'TravelActorNotFoundException',

# ====================== TRAVEL_ACTOR MOVE EXCEPTIONS #======================#
  'TravelActorMovingException',
  'NoInitialPlacementException',
  'ActorAlreadyAtDestinationException',
  'ActorNotOnRosterCannotMoveException',
  'ActorNotOnBoardCannotMoveException',
  'CapturedActorCannotMoveException',

# ====================== TRAVEL_ACTOR SQUARE EXCEPTIONS #======================#
  'PieceSquareNotFoundException',
  'SquareMisMatchesPieceException'
]



class TravelActorException(TravelEventException):
  ERROR_CODE = "TRAVEL_ACTOR_ERROR"
  DEFAULT_MESSAGE = "TravelEvent actor_candidate actor_candidate raised an exception."

#====================== TRAVEL ACTOR VALIDATION EXCEPTIONS #======================#
class NullTravelActorException(TravelActorException, NullException):
  ERROR_CODE = "NULL_TRAVEL_ACTOR_ERROR"
  DEFAULT_MESSAGE = "TravelEvent actor_candidate cannot be null."

class InvalidTravelActorException(TravelActorException, ValidationException):
  ERROR_CODE = "TRAVEL_ACTOR_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "TravelEvent actor_candidate validation failed."

class TravelActorNotFoundException(TravelActorException, InconsistencyException):
  ERROR_CODE = "TRAVEL_ACTOR_NOT_FOUND_ERROR"
  DEFAULT_MESSAGE = (
    "TravelEvent actor_candidate was not found during the board search. There may be a data inconsistency."
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

class ActorNotOnBoardCannotMoveException(TravelActorMovingException):
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
    "The king is checkmated. When a king is checkmated the game ends. If you are seeing this message "
    "the win has not been processed correctly."
  )


# ====================== TRAVEL_ACTOR SQUARE EXCEPTIONS #======================#
class PieceSquareNotFoundException(TravelActorException, InconsistencyException):
  """"""
  ERROR_CODE = "TRAVEL_ACTOR_SQUARE_NOT_FOUND_ERROR"
  DEFAULT_MESSAGE = (
    "BoardSearch did not find a square associated with the actor_candidate's coord. There may be a data "
    "inconsistency."
  )

class SquareMisMatchesPieceException(TravelActorException, InconsistencyException):
  """"""
  ERROR_CODE = "SQUARE_MISMATCHES_TRAVEL_ACTOR_ERROR"
  DEFAULT_MESSAGE = "The square does not contain the actor_candidate. There may be a data inconsistency."
