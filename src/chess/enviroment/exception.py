# src/chess/environment/exception.py

"""
Module: chess.environment.exception
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.1
"""

from chess.system import (
  ChessException, NullException, ValidationException, BuildFailedException, InconsistencyException
)


__all__ = [
  "TurnSceneException",

# ====================== TURN_SCENE GENERAL VALIDATION EXCEPTIONS #======================#
  "NullTurnSceneException",
  "InvalidTurnSceneException",

# ====================== TURN_SCENE ACTOR VALIDATION EXCEPTIONS #======================#
  "CapturedPieceCannotActException",
  "PieceWithNoStartingPlacementException",
  "PieceNotOnRosterCannotActException",
  "PieceNotOnBoardCannotActException",
  "CheckmatedKingCannotActException",

# ====================== TURN_SCENE BUILD EXCEPTIONS #======================#
  "TurnSceneBuildFailedException",

# ====================== TURN_SCENE SQUARE CONSISTENCY EXCEPTIONS #======================#
  "TurnSceneSquareNotFoundException",
  "PieceDoesNotOwnCurrentSquareException",
  "ActorAndScenePropCoordMismatchException",
]


class TurnSceneException(ChessException):
  ERROR_CODE = "TURN_SCENE_ERROR"
  DEFAULT_MESSAGE = "An rollback_exception was raised by a TurnScene."


#====================== TURN_SCENE GENERAL VALIDATION EXCEPTIONS #======================#
class NullTurnSceneException(TurnSceneException, NullException):
  """"""
  ERROR_CODE = "NULL_TURN_SCENE_ERROR"
  DEFAULT_MESSAGE = "A TurnScene cannot be null."


class InvalidTurnSceneException(TurnSceneException, ValidationException):
  """"""
  ERROR_CODE = "TURN_SCENE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "TurnScene validation failed."


# ====================== TURN_SCENE ACTOR VALIDATION EXCEPTIONS #======================#
class CapturedPieceCannotActException(TurnSceneException):
  """"""
  ERROR_CODE = "CAPTURED_PIECE_CANNOT_ACT_ERROR"
  DEFAULT_MESSAGE = "A captured piece cannot act in a scene."


class PieceWithNoStartingPlacementException(TurnSceneException):
  """Raised when team_name potential actor_candidate has not been placed on the board_validator."""
  ERROR_CODE = "PIECE_WITH_NO_INITIAL_PLACEMENT_ERROR"
  DEFAULT_MESSAGE = (
    "A Piece never placed at its starting position cannot act in a scene. A piece never placed "
    "on an initial square cannot act."
  )


class PieceNotOnRosterCannotActException(TurnSceneException):
  """"""
  ERROR_CODE = "PIECE_NOT_ON_ROSTER_CANNOT_ACT_ERROR"
  DEFAULT_MESSAGE = "A Piece must be on its Team roster to act in a scene"
  

class PieceNotOnBoardCannotActException(TurnSceneException):
  """"""
  ERROR_CODE = "PIECE_NOT_ON_BOARD_CANNOT_ACT_ERROR"
  DEFAULT_MESSAGE = "A piece must be on the board to act in a scene,"
  

class CheckmatedKingCannotActException(TurnSceneException):
  """"""
  ERROR_CODE = "CHECK_MATED_KING_CANNOT_ACT_ERROR"
  DEFAULT_MESSAGE = "A checkmated king cannot act in a scene."


# ====================== TURN_SCENE BUILD EXCEPTIONS #======================#
class TurnSceneBuildFailedException(TurnSceneException, BuildFailedException):
  """"""
  ERROR_CODE = "TURN_SCENE_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "TurnScene build failed."
  

# ====================== TURN_SCENE SQUARE CONSISTENCY EXCEPTIONS #======================#
class TurnSceneSquareNotFoundException(TurnSceneException, InconsistencyException):
  """"""
  ERROR_CODE = "TURN_SCENE_SQUARE_NOT_FOUND_ERROR"
  DEFAULT_MESSAGE = (
    "BoardSearch did not find a square associated with the actor_candidate's point. There may be a service "
    "inconsistency."
  )




class ActorAndScenePropCoordMismatchException(TurnSceneException, InconsistencyException):
  """"""
  ERROR_CODE = "ACTOR_AND_SCENE_PROP_COORD_MISMATCH_ERROR"
  DEFAULT_MESSAGE = (
    "The Actor and their Prop have different coords. The scene requires the square and "
    "piece have the same Coord."
  )

