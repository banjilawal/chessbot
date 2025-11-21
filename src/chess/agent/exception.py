# src/chess/agent/collision.py

"""
Module: chess.agent.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ChessException, NullException, ValidationException

__all__ = [
  "PlayerAgentException",

#======================# NULL PLAYER_AGENT EXCEPTIONS #======================#  
  "NullPlayerAgentException",
  
  # ======================# PLAYER_AGENT VALIDATION EXCEPTIONS #======================# 
  "InvalidPlayerAgentException",

#======================# PLAYER_AGENT_BUILD EXCEPTIONS #======================#  
  "PlayerAgentBuildFailedException",
]




class PlayerAgentException(ChessException):
  """
  Super class for exceptions raised by Agent objects. DO NOT USE DIRECTLY. Subclasses
  give more useful debugging messages.
  """
  ERROR_CODE = "PLAYER_AGENT_ERROR"
  DEFAULT_MESSAGE = "Agent raised an exception"

#======================# PLAYER_AGENT_VALIDATION EXCEPTIONS #======================#  
class NullPlayerAgentException(PlayerAgentException, NullException):
  """Raised if an entity, method, or operation requires team_name agent but gets null instead."""
  ERROR_CODE = "NULL_PLAYER_AGENT_ERROR"
  DEFAULT_MESSAGE = f"Agent cannot be null"

class InvalidPlayerAgentException(PlayerAgentException, ValidationException):
  """
  Raised by PlayerAgentValidator if a candidate fails sanity checks. Exists primarily to catch all exceptions raised
  validating an existing Agent object.
  """
  ERROR_CODE = "PLAYER_AGENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Agent validation failed."

#======================# PLAYER_AGENT_BUILD EXCEPTIONS #======================#  
class PlayerAgentBuildFailedException(PlayerAgentException, BuildFailedException):
  """
  Raised when PlayerAgentBuilder encounters an error building a new Agent instance. Exists
  primarily as a catchall.
  """
  ERROR_CODE = "PLAYER_AGENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Agent build failed."
#
# #======================# PLAYER_AGENT_HISTORY EXCEPTIONS #======================#
# class PlayerAgentHistoryException(PlayerAgentException):
#   """Team list specific errors."""
#   ERROR_CODE = "PLAYERAGENT_HISTORY_ERROR"
#   DEFAULT_MESSAGE = "PlayerAgentHistory raised an exception."
#
# class InconsistentCommandHistoryException(PlayerAgentHistoryException, InconsistentCollectionException):
#   ERROR_CODE = "INCONSISTENT_PLAYERAGENT_HISTORY_ERROR"
#   DEFAULT_MESSAGE = (
#     "PlayerAgentHistory is an inconsistent state. Data might be corrupt."
#   )
#
# class PushNewTeamException(PlayerAgentHistoryException):
#   """Raised if team_name new team_name could not be pushed to commandHistory"""
#   ERROR_CODE = "PUSH_NEW_TEAM_ERROR"
#   DEFAULT_MESSAGE = "Could not push team_name new team_name to TeamStack."
#
# class UndoingPushTeamFailedException(PlayerAgentHistoryException):
#   """Raised if removing the current team_name failed"""
#   ERROR_CODE = "UNDOING_PUSH_TEAM_FAILED_ERROR"
#   DEFAULT_MESSAGE = "Could not undo the new team_name addition."
#
# class CannotRemoveOldTeamException(PlayerAgentHistoryException):
#   """Raised if an attempt is made to remove an old team_name from TeamStack"""
#   ERROR_CODE = "REMOVE_OLD_TEAM_ERROR"
#   DEFAULT_MESSAGE = "Removing old teams from TeamStack is not allowed."
#
# class InvalidPlayerAgentAssignmentException(PlayerAgentHistoryException):
#   """
#   If team_name team_name already attached to team_name agent (team_name.agent == not None) tries being assigned team_name
#   different agent, `InvalidPlayerAgentAssignmentException` is raised.
#   """
#   ERROR_CODE = "INVALID_PLAYERAGENT_ASSIGNMENT_ERROR"
#   DEFAULT_MESSAGE = "Team is already assigned to team_name different agent."




