# src/chess/environment/collision.py

"""
Module: chess.environment.exception
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.1
"""

from chess.system import (
    ChessException, NullException, ValidationException, BuildException, InconsistencyException
)


__all__ = [
  "TurnSceneException",

#====================== TURN_SCENE GENERAL VALIDATION EXCEPTION #======================#
  "NullTurnSceneException",
  "InvalidTurnSceneException",

#====================== TURN_SCENE ACTOR VALIDATION EXCEPTION #======================#
  "DisabledHostagePieceException",
  "PieceWithNoStartingPlacementException",
  "DisabledUnRosteredPieceCannotActException",
  "PieceNotOnBoardCannotActException",
  "CheckmatedKingCannotActException",

#====================== TURN_SCENE BUILD EXCEPTION #======================#
    "TurnSceneBuildException",

#====================== TURN_SCENE SQUARE CONSISTENCY EXCEPTION #======================#
  "TurnSceneSquareNotFoundException",
  "PieceDoesNotOwnCurrentSquareException",
  "ActorAndScenePropCoordMismatchException",
]


class TurnSceneException(ChessException):
  ERROR_CODE = "TURN_SCENE_ERROR"
  DEFAULT_MESSAGE = "An rollback_exception was raised by a TurnScene."


#====================== TURN_SCENE GENERAL VALIDATION EXCEPTION #======================#
class NullTurnSceneException(TurnSceneException, NullException):
  """"""
  ERROR_CODE = "NULL_TURN_SCENE_ERROR"
  DEFAULT_MESSAGE = "A TurnScene cannot be null."


class InvalidTurnSceneException(TurnSceneException, ValidationException):
  """"""
  ERROR_CODE = "TURN_SCENE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "TurnScene validation failed."


#====================== TURN_SCENE ACTOR VALIDATION EXCEPTION #======================#

  




#====================== TURN_SCENE BUILD EXCEPTION #======================#
class TurnSceneBuildException(TurnSceneException, BuildException):
  """"""
  ERROR_CODE = "TURN_SCENE_BUILD_FAILED"
  DEFAULT_MESSAGE = "TurnScene build failed."
  

#====================== TURN_SCENE SQUARE CONSISTENCY EXCEPTION #======================#
class TurnSceneSquareNotFoundException(TurnSceneException, InconsistencyException):
  """"""
  ERROR_CODE = "TURN_SCENE_SQUARE_NOT_FOUND_ERROR"
  DEFAULT_MESSAGE = (
    "BoardSearch did not find a square_name associated with the actor_candidate's point. There may be a entity_service "
    "inconsistency."
  )




class ActorAndScenePropCoordMismatchException(TurnSceneException, InconsistencyException):
  """"""
  ERROR_CODE = "ACTOR_AND_SCENE_PROP_COORD_MISMATCH_ERROR"
  DEFAULT_MESSAGE = (
    "The Actor and their Prop have different coords. The scene requires the square_name and "
    "piece have the same Coord."
  )

