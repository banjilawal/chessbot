# src/chess.coord.exception.py

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
**Comprehensive Domain Error Catalog.** The central theme is to provide a
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

from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
  'ContextException',

# === CONTEXT VALIDATION EXCEPTIONS ===
  'NullContextException',
  'InvalidContextException',

# === CONTEXT BUILD EXCEPTIONS ===
  'ContextBuildFailedException',

# === CONTEXT HISTORY EXCEPTIONS ===
  'ContextHistoryException',
  'InconsistentCommandHistoryException',
  'PushNewTeamException',
  'UndoingPushTeamFailedException',
  'InvalidContextAssignmentException'
]

class ContextException(ChessException):
  """
  Super class for exceptions raised by Context objects. DO NOT
  USE DIRECTLY. Subclasses give more useful debugging messages.
  """
  ERROR_CODE = "CONTEXT_ERROR"
  DEFAULT_MESSAGE = "Context raised an team_exception"

# === CONTEXT VALIDATION EXCEPTIONS ===
class NullContextException(ContextException, NullException):
  """
  Raised if an entity, method, or operation requires a context but
  gets null instead.
  """
  ERROR_CODE = "NULL_CONTEXT_ERROR"
  DEFAULT_MESSAGE = f"Context cannot be null"

class InvalidContextException(ContextException, ValidationException):
  """
  Raised by BoardValidator if board fails sanity checks. Exists primarily to
  catch all exceptions raised validating an existing board
  """
  ERROR_CODE = "CONTEXT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Context validate failed"

# === CONTEXT BUILD EXCEPTIONS ===
class ContextBuildFailedException(ContextException, BuildFailedException):
  """
  Raised when BoardBuilder encounters an error while building a team. Exists primarily to catch all
  exceptions raised build a new board
  """
  ERROR_CODE = "CONTEXT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Context build failed."

# === CONTEXT HISTORY EXCEPTIONS ===
class ContextHistoryException(ContextException):
  """Team list specific errors."""
  ERROR_CODE = "CONTEXT_HISTORY_ERROR"
  DEFAULT_MESSAGE = "ContextHistory raised an exception."

class InconsistentCommandHistoryException(ContextHistoryException, InconsistentCollectionException):
  ERROR_CODE = "INCONSISTENT_CONTEXT_HISTORY_ERROR"
  DEFAULT_MESSAGE = (
    "ContextHistory is an inconsistent state. Data might be corrupt."
  )

class PushNewTeamException(ContextHistoryException):
  """Raised if a new team could not be pushed to commandHistory"""
  ERROR_CODE = "PUSH_NEW_TEAM_ERROR"
  DEFAULT_MESSAGE = "Could not push a new team to CommandHistory."

class UndoingPushTeamFailedException(ContextHistoryException):
  """Raised if removing the current team failed"""
  ERROR_CODE = "UNDOING_PUSH_TEAM_FAILED_ERROR"
  DEFAULT_MESSAGE = "Could not undo the new team addition."

class CannotRemoveOldTeamException(ContextHistoryException):
  """Raised if an attempt is made to remove an old team from CommandHistory"""
  ERROR_CODE = "REMOVE_OLD_TEAM_ERROR"
  DEFAULT_MESSAGE = "Removing old teams from CommandHistory is not allowed."

class InvalidContextAssignmentException(ContextHistoryException):
  """
  If a team already attached to a context (team.context == not None) tries being assigned a
  different context, `InvalidContextAssignmentException` is raised.
  """
  ERROR_CODE = "INVALID_CONTEXT_ASSIGNMENT_ERROR"
  DEFAULT_MESSAGE = "Team is already assigned to a different context."






class ContextException(ChessException):
  """
  """
  ERROR_CODE = "CONTEXT_ERROR"
  DEFAULT_MESSAGE = "Context raised an exception."


class NullContextException(ChessException, NullException):
  """
  """
  ERROR_CODE = "NULL_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "Context cannot be null."


class SearchContextException(ContextException):
  """
  """
  ERROR_CODE = "SEARCH_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "SearchContext raised an exception."

  class SearchContextException(ContextException):
    """
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "SearchContext raised an exception."


class NullSearchContextException(SearchContextException, NullContextException):
  """
  """
  ERROR_CODE = "NULL_SEARCH_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "SearchContext cannot be null."
  
  
class FilterContextException(SearchContextException):
  """
  """
  ERROR_CODE = "FILTER_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "FilterContext raised an exception."


class NullFilterContextException(NullSearchContextException):
  """
  """
  ERROR_CODE = "NULL_SEARCH_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "SearchContext cannot be null."
  

class InvalidContextException(ContextException):
  from chess.exception import RollbackException
  from chess.piece.event import OccupationEventException

 