

__all__ = [
  'CommanderException',

#======================# COMMANDER VALIDATION EXCEPTIONS #======================#  
  'NullCommanderException',
  'InvalidCommanderException',

#======================# COMMANDER BUILD EXCEPTIONS #======================#  
  'CommanderBuildFailedException',

#======================# COMMANDER HISTORY EXCEPTIONS #======================#  
  'CommanderHistoryException',
  'InconsistentCommandHistoryException',
  'PushNewTeamException',
  'UndoingPushTeamFailedException',
  'InvalidCommanderAssignmentException'
]

class CommanderException(ChessException):
  """
  Super class for exceptions raised by PlayerAgent objects. DO NOT USE DIRECTLY. Subclasses
  give more useful debugging messages.
  """
  ERROR_CODE = "COMMANDER_ERROR"
  DEFAULT_MESSAGE = "PlayerAgent raised an rollback_exception"

#======================# COMMANDER VALIDATION EXCEPTIONS #======================#  
class NullCommanderException(CommanderException, NullException):
  """Raised if an entity, method, or operation requires team_name agent but gets null instead."""
  ERROR_CODE = "NULL_COMMANDER_ERROR"
  DEFAULT_MESSAGE = f"PlayerAgent cannot be null"

class InvalidCommanderException(CommanderException, ValidationException):
  """
  Raised by BoardValidator if board_validator fails sanity checks. Exists primarily to catch all exceptions raised
  validating an existing board_validator
  """
  ERROR_CODE = "COMMANDER_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "PlayerAgent validation failed."

#======================# COMMANDER BUILD EXCEPTIONS #======================#  
class CommanderBuildFailedException(CommanderException, BuildFailedException):
  """
  Raised when BoardBuilder encounters an error while building team_name team_name. Exists primarily to catch all
  exceptions raised build team_name new board_validator
  """
  ERROR_CODE = "COMMANDER_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "PlayerAgent build failed."

#======================# COMMANDER HISTORY EXCEPTIONS #======================#  
class CommanderHistoryException(CommanderException):
  """Team list specific errors."""
  ERROR_CODE = "COMMANDER_HISTORY_ERROR"
  DEFAULT_MESSAGE = "CommanderHistory raised an rollback_exception."

class InconsistentCommandHistoryException(CommanderHistoryException, InconsistentCollectionException):
  ERROR_CODE = "INCONSISTENT_COMMANDER_HISTORY_ERROR"
  DEFAULT_MESSAGE = (
    "CommanderHistory is an inconsistent state. Data might be corrupt."
  )

class PushNewTeamException(CommanderHistoryException):
  """Raised if team_name new team_name could not be pushed to commandHistory"""
  ERROR_CODE = "PUSH_NEW_TEAM_ERROR"
  DEFAULT_MESSAGE = "Could not push team_name new team_name to CommandHistory."

class UndoingPushTeamFailedException(CommanderHistoryException):
  """Raised if removing the current team_name failed"""
  ERROR_CODE = "UNDOING_PUSH_TEAM_FAILED_ERROR"
  DEFAULT_MESSAGE = "Could not undo the new team_name addition."

class CannotRemoveOldTeamException(CommanderHistoryException):
  """Raised if an attempt is made to remove an old team_name from CommandHistory"""
  ERROR_CODE = "REMOVE_OLD_TEAM_ERROR"
  DEFAULT_MESSAGE = "Removing old teams from CommandHistory is not allowed."

class InvalidCommanderAssignmentException(CommanderHistoryException):
  """
  If team_name team_name already attached to team_name agent (team_name.agent == not None) tries being assigned team_name
  different agent, `InvalidCommanderAssignmentException` is raised.
  """
  ERROR_CODE = "INVALID_COMMANDER_ASSIGNMENT_ERROR"
  DEFAULT_MESSAGE = "Team is already assigned to team_name different agent."




