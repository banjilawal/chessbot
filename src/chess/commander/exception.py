# src/chess/vector/rollback_exception.py

"""
Module: chess.vector.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, validator, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each consistency and behavior in the `Vector` class has an rollback_exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` graph.
2. Fast debugging using highly granular rollback_exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` graph.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
"""

from chess.system import(
  ChessException,
  NullException,
  BuildFailedException,
  ValidationException,
  InconsistentCollectionException
)

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
  Super class for exceptions raised by Commander objects. DO NOT USE DIRECTLY. Subclasses
  give more useful debugging messages.
  """
  ERROR_CODE = "COMMANDER_ERROR"
  DEFAULT_MESSAGE = "Commander raised an rollback_exception"

#======================# COMMANDER VALIDATION EXCEPTIONS #======================#  
class NullCommanderException(CommanderException, NullException):
  """Raised if an entity, method, or operation requires team_name commander but gets null instead."""
  ERROR_CODE = "NULL_COMMANDER_ERROR"
  DEFAULT_MESSAGE = f"Commander cannot be null"

class InvalidCommanderException(CommanderException, ValidationException):
  """
  Raised by BoardValidator if board_validator fails sanity checks. Exists primarily to catch all exceptions raised
  validating an existing board_validator
  """
  ERROR_CODE = "COMMANDER_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Commander validation failed."

#======================# COMMANDER BUILD EXCEPTIONS #======================#  
class CommanderBuildFailedException(CommanderException, BuildFailedException):
  """
  Raised when BoardBuilder encounters an error while building team_name team_name. Exists primarily to catch all
  exceptions raised build team_name new board_validator
  """
  ERROR_CODE = "COMMANDER_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Commander build failed."

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
  If team_name team_name already attached to team_name commander (team_name.commander == not None) tries being assigned team_name
  different commander, `InvalidCommanderAssignmentException` is raised.
  """
  ERROR_CODE = "INVALID_COMMANDER_ASSIGNMENT_ERROR"
  DEFAULT_MESSAGE = "Team is already assigned to team_name different commander."




