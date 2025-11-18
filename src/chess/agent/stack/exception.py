# src/chess/agent/stack/exception.py

"""
Module: chess.agent.stack.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.system import ChessException, ValidationException, NullException


__all__ = [
  "TeamStackException",
  
# ======================# NULL TEAM_STACK EXCEPTIONS #======================#
  "NullTeamStackException",
  
# ======================# TEAM_STACK VALIDATION EXCEPTIONS #======================#
  "InvalidTeamStackException",
  "TeamStackSizeConflictException",
  "InconsistentCurrentTeamException",
  "CorruptedTeamStackException",

# ======================# TEAM_STACK OPERATION EXCEPTIONS #======================#
  "PoppingEmptyTeamStackException",
  "PushingDuplicateTeamException",
  "PushingNullException",

# ======================# TEAM_STACK_SERVICE EXCEPTIONS #======================#
  "TeamStackServiceException",

# ======================# NULL TEAM_STACK_SERVICE EXCEPTIONS #======================#
  "NullTeamStackServiceException",


# ======================# TEAM_STACK VALIDATION EXCEPTIONS #======================#
  "InvalidTeamStackServiceException",
]


class TeamStackException(ChessException):
  """
  Super class for exceptions raised by TeamStack objects. DO NOT USE DIRECTLY. Subclasses
  give more useful debugging messages.
  """
  ERROR_CODE = "TEAM_STACK_ERROR"
  DEFAULT_MESSAGE = "TeamStack raised an exception."


# ======================# NULL TEAM_STACK EXCEPTIONS #======================#
class NullTeamStackException(TeamStackException, NullException):
  """Raised if an entity, method, or operation requires TeamStack but gets null instead."""
  ERROR_CODE = "NULL_TEAM_STACK_ERROR"
  DEFAULT_MESSAGE = "TeamStack cannot be null."


# ======================# TEAM_STACK VALIDATION EXCEPTIONS #======================#
class InvalidTeamStackException(TeamStackException, ValidationException):
  """Catchall Exception for TeamStackValidator when a validation candidate fails a sanity check."""
  ERROR_CODE = "TEAM_STACK_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "TeamStack validation failed."


class TeamStackSizeConflictException(TeamStackException, ValidationException):
  """Raised if team_stack.size and team_stack.is_empty() contradict each other."""
  ERROR_CODE = "TEAM_STACK_SIZE_CONFLICT_ERROR"
  DEFAULT_MESSAGE = "TeamStack.size and TeamStack.is_empty() give contradictory results."


class InconsistentCurrentTeamException(TeamStackException, ValidationException):
  """Raised if team_stack.current_team is not null but the stack is empty or vice versa."""
  ERROR_CODE = "INCONSISTENT_CURRENT_TEAM_ERROR"
  DEFAULT_MESSAGE = "The TeamStack.current_team contradicts the stack's emptyness state."


class CorruptedTeamStackException(TeamStackException, ValidationException):
  """RAised if the list is null. That is TeamStack.items is null"""
  ERROR_CODE = "CORRUPTED_TEAM_STACK_ERROR"
  DEFAULT_MESSAGE = "TeamStack.items is null. There is inconsistent data in the system."


# ======================# TEAM_STACK OPERATION EXCEPTIONS #======================#
class PoppingEmptyTeamStackException(TeamStackException):
  """Raised when trying to pop from an empty TeamStack."""
  ERROR_CODE = "POPPING_EMPTY_STACK_ERROR"
  DEFAULT_MESSAGE = "Cannot pop from an empty TeamStack."

class PushingDuplicateTeamException(TeamStackException):
  """Raised when trying to push the same team onto the stack."""
  ERROR_CODE = "PUSHING_DUPLICATE_TEAM_ERROR"
  DEFAULT_MESSAGE = "Cannot push duplicate team onto the stack. All Teams must be unique."

class PushingNullException(TeamStackException):
  """Raised when trying to push null item to stack."""
  ERROR_CODE = "PUSHING_NULL_ERROR"
  DEFAULT_MESSAGE = "Cannot push null item onto a TeamStack."


# ======================# TEAM_STACK_SERVICE EXCEPTIONS #======================#
class TeamStackServiceException(ChessException):
  """
  Super class for exceptions raised by TeamStackService objects. DO NOT USE DIRECTLY. Subclasses
  give more useful debugging messages.
  """
  ERROR_CODE = "TEAM_STACK_SERVICE_ERROR"
  DEFAULT_MESSAGE = "TeamStackService raised an exception."


# ======================# NULL TEAM_STACK_SERVICE EXCEPTIONS #======================#
class NullTeamStackServiceException(TeamStackServiceException, NullException):
  """Raised if an entity, method, or operation requires TeamStackService but gets null instead."""
  ERROR_CODE = "NULL_TEAM_STACK_SERVICE_ERROR"
  DEFAULT_MESSAGE = "TeamStackService cannot be null."


# ======================# TEAM_STACK VALIDATION EXCEPTIONS #======================#
class InvalidTeamStackServiceException(TeamStackServiceException, ValidationException):
  """Catchall Exception for TeamStackServiceValidator when a validation candidate fails a sanity check."""
  ERROR_CODE = "TEAM_STACK_SERVICE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "TeamStackService validation failed."



