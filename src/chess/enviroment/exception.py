# src/chess/environment/exception.py

"""
Module: `chess.environment.exception`
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.1
"""

from chess.piece import TravelEventException
from chess.system import ChessException, NullException, ValidationException, InconsistencyException

__all__ = [
  'BoardActorException',
  'TravelResourceException',

#====================== TravelEvent actor_candidate VALIDATION EXCEPTIONS #======================#
  'InvalidBoardActorException',
  'InvalidTravelResourceException',
  'NullBoardActorException',
  'NullTravelResourceException',
  'BoardActorNotFoundException',
  
  'NullTravelerEnvironmentTupleException',
  'NullDestinationEnvironmentTupleException',

# ====================== TRAVEL_ACTOR MOVE EXCEPTIONS #======================#
  'BoardActorMovingException',
  'NoInitialPlacementException',
  'ActorAlreadyAtDestinationException',
  'ActorNotOnRosterCannotMoveException',
  'BoardPieceRemovedCannotActException',
  'CapturedActorCannotMoveException',

# ====================== TRAVEL_ACTOR SQUARE EXCEPTIONS #======================#
  'BoardActorSquareNotFoundException',
  'SquareMisMatchesBoardActorException'
]


class BoardActorException(ChessException):
  ERROR_CODE = "BOARD_ACTOR_ERROR"
  DEFAULT_MESSAGE = "An rollback_exception was raised by a TravelEvent traveler."


class TravelResourceException(TravelEventException):
  ERROR_CODE = "TRAVEL_RESOURCE_ERROR"
  DEFAULT_MESSAGE = "An rollback_exception was raised by a TravelEvent resource."

#====================== TRAVEL ACTOR VALIDATION EXCEPTIONS #======================#
class NullBoardActorException(BoardActorException, NullException):
  ERROR_CODE = "NULL_BOARD_ACTOR_ERROR"
  DEFAULT_MESSAGE = "A TravelEvent traveler cannot be null."

class NullTravelResourceException(TravelResourceException, NullException):
  ERROR_CODE = "NULL_TRAVEL_RESOURCE_ERROR"
  DEFAULT_MESSAGE = "A TravelEvent resource cannot be null."

class NullTravelerEnvironmentTupleException(BoardActorException, NullException):
  ERROR_CODE = "NULL_TRAVELER_ENVIRONMENT_TUPLE_ERROR"
  DEFAULT_MESSAGE = "Piece-Board-Tuple passed to BoardActorValidator cannot be null."
  
class NullDestinationEnvironmentTupleException(TravelResourceException, NullException):
  ERROR_CODE = "NULL_DESTINATION__ENVIRONMENT_TUPLE_ERROR"
  DEFAULT_MESSAGE = "Square-Board-Tuple passed to BoardResourceValidator cannot be null."

class InvalidBoardActorException(BoardActorException, ValidationException):
  ERROR_CODE = "BOARD_ACTOR_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Validation of a TravelEvent traveler failed."

class InvalidTravelResourceException(TravelResourceException, ValidationException):
  ERROR_CODE = "TRAVEL_RESOURCE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Validation of a TravelEvent resource failed."

class BoardActorNotFoundException(BoardActorException, InconsistencyException):
  ERROR_CODE = "BOARD_ACTOR_NOT_FOUND_ERROR"
  DEFAULT_MESSAGE = (
    "TravelEvent actor_candidate was not found during the board search. There may be a service inconsistency."
  )

# ====================== TRAVEL_ACTOR MOVE EXCEPTIONS #======================#
class BoardActorMovingException(BoardActorException):
  ERROR_CODE = "BOARD_ACTOR_MOVE_ERROR"
  DEFAULT_MESSAGE = "TravelEvent actor_candidate raised a moving violation. Candidate cannot travel."

class NoInitialPlacementException(BoardActorMovingException):
  """"""
  ERROR_CODE = "ACTOR_DID_NOT_HAVE_INITIAL_PLACEMENT_ERROR"
  DEFAULT_MESSAGE = (
    "TravelEvent actor_candidate did not have an initial placement on the board. Its position history is empty. "
    "Candidate cannot travel."
  )

class ActorAlreadyAtDestinationException(BoardActorMovingException):
  """"""
  ERROR_CODE = "ACTOR_ALREADY_AT_DESTINATION_ERROR"
  DEFAULT_MESSAGE = "TravelEvent actor_candidate is already at the destination square. There is nn need to travel."

class ActorNotOnRosterCannotMoveException(BoardActorMovingException):
  """"""
  ERROR_CODE = "ACTOR_NOT_ON_ROSTER_MOVE_ERROR"
  DEFAULT_MESSAGE = "TravelEvent actor_candidate is not on their team_name's roster. Candidate cannot travel."

class BoardPieceRemovedCannotActException(BoardActorMovingException):
  """"""
  ERROR_CODE = "ACTOR_NOT_ON_BOARD_MOVE_ERROR"
  DEFAULT_MESSAGE = (
    "TravelEvent actor_candidate is not on the board. Candidate cannot travel."
  )

class CapturedActorCannotMoveException(BoardActorMovingException):
  """"""
  ERROR_CODE = "CAPTURED_ACTOR_MOVE_ERROR"
  DEFAULT_MESSAGE = (
    "TravelEvent actor_candidate has been captured by the enemy. Captured pieces are not on the board."
    "Candidate cannot travel."
  )

class CheckMatedKingCannotMoveException(BoardActorMovingException):
  """"""
  ERROR_CODE = "CHECK_MATED_KING_MOVE_ERROR"
  DEFAULT_MESSAGE = (
    "The occupation is checkmated. When a occupation is checkmated the game ends. If you are seeing this message "
    "the win has not been processed correctly."
  )


# ====================== TRAVEL_ACTOR SQUARE EXCEPTIONS #======================#
class BoardActorSquareNotFoundException(BoardActorException, InconsistencyException):
  """"""
  ERROR_CODE = "BOARD_ACTOR_SQUARE_NOT_FOUND_ERROR"
  DEFAULT_MESSAGE = (
    "BoardSearch did not find a square associated with the actor_candidate's point. There may be a service "
    "inconsistency."
  )

class SquareMisMatchesBoardActorException(BoardActorException, InconsistencyException):
  """"""
  ERROR_CODE = "SQUARE_MISMATCHES_BOARD_ACTOR_ERROR"
  DEFAULT_MESSAGE = "The square does not contain the actor_candidate. There may be a service inconsistency."
