# src/chess.coord.rollback_exception.py

"""
Module: chess.coord.rollback_exception
Author: Banji Lawal
Created: 2025-09-16
Updated: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, validation, and manipulation of `Team` objects.

***Limitations***: It does not contain any logic for raising these exceptions; that responsibility
    `Team`, `TeamBuilder`, and `TeamValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each field and behavior in the `Team` class has an rollback_exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Team` domain.
2. Fast debugging using highly granular rollback_exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Team` domain.
4. Providing a clear distinction between errors related to `Team` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `TeamException`,
`NullTeamException`, `InvalidTeamException`, ).
"""


from chess.system import(
  ChessException, SearchException, NullException, ValidationException, BuildFailedException, RollbackException
)

__all__ = [
  'TeamException',
  'TeamRollBackException',

#======================# TEAM VALIDATION EXCEPTIONS #======================#  
  'NullTeamException',
  'InvalidTeamException',

#======================# TEAM BUILD EXCEPTIONS #======================#  
  'TeamBuildFailedException',

#======================# TEAM MEMBER EXCEPTIONS #======================#  
  'TeamRosterException',
  'AddTeamMemberException',
  'AddEnemyToRosterException',
  'RemoveTeamMemberException',
  'FullRankQuotaException',

#======================# TEAM MEMBER EXCEPTIONS WITH ROLLBACK #======================#  
  'TeamRosterRollBackException',
  'AddEnemyHostageRolledBackException',
  'AddTeamMemberRolledBackException',
  'RemoveTeamMemberRolledBackException',
  'FullRankQuotaRolledBackException',
  'ConflictingTeamAssignmentException',

#======================# HOSTAGE EXCEPTIONS #======================#  
  'TeamHostageListException',
  'InconsistentHostageEntry',
  'InvalidFriendlyHostageException',
  'AddEnemyHostageException',
  'AddEnemyKingHostageException',
  'HostageRemovalException',

#======================# HOSTAGE EXCEPTIONS WITH ROLLBACK #======================#  
  'TeamHostageListRolledBackException',
  'InvalidFriendlyHostageRolledBackException',
  'AddEnemyToRosterRolledBackException',
  'EnemyKingHostageRolledBackException',
  'HostageRemovalRolledBackException',

#======================# SEARCH EXCEPTIONS #======================#  
  'RosterNumberOutOfBoundsException'
]

class TeamException(ChessException):
  """
  Super class of all exceptions `Team` object raises. Do not use directly. Subclasses give
  details useful for debugging. This class exists primarily to allow catching all `Team`
  exceptions.
  """
  ERROR_CODE = "TEAM_ERROR"
  DEFAULT_MESSAGE = "Team raised an rollback_exception."

class TeamRollBackException(TeamException):
  """
  Super class for exceptions that require `Team` and related object be rolled back to maintain
  integrity`.
  """
  pass
  ERROR_CODE = "TEAM_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Team raised an rollback_exception. Transaction rollback performed."


#======================# TEAM VALIDATION EXCEPTIONS #======================#  
class NullTeamException(TeamException, NullException):
  """Raised if an entity, method, or operation requires `Team` but gets null instead."""
  ERROR_CODE = "NULL_TEAM_ERROR"
  DEFAULT_MESSAGE = "Team cannot be null"

class InvalidTeamException(TeamException, ValidationException):
  """
  Raised by `TeamValidator` if an object fails sanity checks. Exists primarily to catch all
  exceptions raised validating an existing`Team`.
  """
  ERROR_CODE = "TEAM_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Team validation failed"


#======================# TEAM BUILD EXCEPTIONS #======================#  
class TeamBuildFailedException(TeamException, BuildFailedException):
  """
  Raised when TeamBuilder encounters an error while building `Team`. Exists primarily to
  catch all exceptions raised building team new team
  """
  ERROR_CODE = "TEAM_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Team build failed."


#======================# TEAM MEMBER LIST EXCEPTIONS #======================#  
class TeamRosterException(TeamException):
  """Raised for errors on team's roster"""
  ERROR_CODE = "TEAM_ROSTER_ERROR"
  DEFAULT_MESSAGE = "Team roster raised an rollback_exception."

class AddTeamMemberException(TeamRosterException):
  """Raised if piece could not be added to the team's roster"""
  ERROR_CODE = "ADD_TEAM_MEMBER_ERROR"
  DEFAULT_MESSAGE = "Could not add piece to team's roster."

class AddEnemyToRosterException(TeamRosterException):
  """Attempting to add an enemy to the team's roster raises an rollback_exception."""
  ERROR_CODE = "ADD_ENEMY_TO_ROSTER_ERROR"
  DEFAULT_MESSAGE = "An enemy piece cannot be added to the team's roster."

class RemoveTeamMemberException(TeamRosterException):
  """Raised if piece could not be removed from the team's roster"""
  ERROR_CODE = "REMOVE_TEAM_MEMBER_ERROR"
  DEFAULT_MESSAGE = "Could not remove team piece to team's roster."

class FullRankQuotaException(TeamRosterException):
  """Raised if the team has not empty slots for the piece's rank."""
  ERROR_CODE = "FULL_RANK_QUOTA_ERROR"
  DEFAULT_MESSAGE = "The team has no empty slots for the piece's rank."

class ConflictingTeamAssignmentException(TeamRosterException):
  """
  If team piece that's already on one team (piece.team == not None) tries joining
  another InvalidTeamAssignmentException is raised.
  """
  ERROR_CODE = "CONFLICTING_TEAM_ASSIGNMENT_ERROR"
  DEFAULT_MESSAGE = "Piece is already assigned to team team."


#======================# TEAM MEMBER LIST EXCEPTIONS WITH ROLLBACK #======================#  
class TeamRosterRollBackException(TeamRosterException, RollbackException):
  """Raised for errors on team's roster that are raised after rollback."""
  ERROR_CODE = "TEAM_ROSTER_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Team roster raised an rollback_exception. Transaction rollback performed."

class AddTeamMemberRolledBackException(TeamRosterRollBackException):
  """
  Raised if team notification failed to add team piece could to the team's roster; then the
  notification was rolled back before raising this err.
  """
  ERROR_CODE = "ADD_TEAM_MEMBER_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Adding piece to team's roster failed. Transaction rollback performed."
  )

class AddEnemyToRosterRolledBackException(TeamRosterRollBackException):
  """
  Raised if team notification attempted to add an enemy to the team's roster.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "ADD_ENEMY_TO_ROSTER_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Caught attempt to add an enemy piece to the team's roster Transaction "
    "rollback performed."
  )

class RemoveTeamMemberRolledBackException(TeamRosterRollBackException):
  """
  Raised if team notification failed to remove team piece from the team's roster. The
  notification was rolled back before raising this err.
  """
  ERROR_CODE = "REMOVE_TEAM_MEMBER_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Could not remove team piece from the team's roster. Transaction rollback performed."
  )

class FullRankQuotaRolledBackException(TeamRosterRollBackException):
  """
  Raised if team notification failed could not add team piece because there were no empty slots
  for the piece's rank. The notification was rolled back before raising this err.
  """
  ERROR_CODE = "FULL_RANK_QUOTA_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "The team has no empty slots for the piece's rank. Transaction rollback performed."
  )

class ConflictingTeamAssignmentRolledBackException(TeamRosterRollBackException):
  """
  Raised if team notification tries to assign team piece to team different team's roster.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "CONFLICTING_TEAM_ASSIGNMENT_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Piece is already assigned to team team. Transaction rollback performed."
  )

#======================# HOSTAGE LIST EXCEPTIONS #======================#  
class TeamHostageListException(TeamException):
  """Raised on errors with team's hostage list"""
  ERROR_CODE = "TEAM_HOSTAGE_LIST_ERROR"
  DEFAULT_MESSAGE = "Team hostage list raised an rollback_exception."


class InconsistentHostageEntry(TeamHostageListException):
  """Raised on errors where a hostage shouldn't be in the  hostage list, i.e captor == null"""
  ERROR_CODE = "INCONSISTENT_HOSTAGE_ENTRY_ERROR"
  DEFAULT_MESSAGE = "An enemy with no captor is in the hostage list. There may be inconsistent data."

class InvalidFriendlyHostageException(TeamHostageListException):
  """Attempting to team friendly to the hostage list raises an rollback_exception."""
  ERROR_CODE = "INVALID_FRIENDLY_HOSTAGE_ERROR"
  DEFAULT_MESSAGE = "A friendly piece cannot be added to the team's hostage list"

class AddEnemyHostageException(TeamHostageListException):
  """Raised if team piece could not be added to the team's hostage list"""
  ERROR_CODE = "ADD_ENEMY_HOSTAGE_ERROR"
  DEFAULT_MESSAGE = "Could not add an enemy piece to the team's hostage list"

class AddEnemyKingHostageException(TeamHostageListException):
  """Attempting to an enemy king to the hostage list raises an rollback_exception."""
  ERROR_CODE = "ADD_ENEMY_KING_HOSTAGE_ERROR"
  DEFAULT_MESSAGE = (
    "An enemy king cannot be added to the team's hostage list. Kings can only "
    "be checked or checkmated"
  )

class HostageRemovalException(TeamHostageListException):
  """Attempting to remove an enemy from the hostage list raises an rollback_exception."""
  ERROR_CODE = "HOSTAGE_REMOVAL_ERROR"
  DEFAULT_MESSAGE = "An enemy piece cannot be removed from the team's hostage list"


#======================# HOSTAGE LIST EXCEPTIONS WITH ROLLBACK #======================#  
class TeamHostageListRolledBackException(TeamHostageListException, RollbackException):
  """
  Raised on transactions that raise hostage list errors. Exception is raised after
  the notification is rolled back.
  """
  ERROR_CODE = "TEAM_HOSTAGE_LIST_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Team hostage list raised an rollback_exception. Transaction rollback performed."
  )

class InvalidFriendlyHostageRolledBackException(TeamHostageListRolledBackException):
  """
  Raised if team notification attempts to add team friendly piece to the team's hostage list.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "INVALID_FRIENDLY_HOSTAGE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "A friendly piece cannot be added to the team's hostage list"

class AddEnemyHostageRolledBackException(TeamHostageListRolledBackException):
  """
  Raised if team notification could not add an enemy piece to the team's hostage list.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "ADD_ENEMY_HOSTAGE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Could not add an enemy piece to the team's hostage list."


class EnemyKingHostageRolledBackException(TeamHostageListRolledBackException):
  """
  Raised if team notification attempted adding an enemy king to the team's hostage list.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "ADD_ENEMY_KING_HOSTAGE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "An enemy king cannot be added to the team's hostage list. Kings can only "
    "be checked or checkmated."
  )

class HostageRemovalRolledBackException(TeamHostageListRolledBackException):
  """
  Raised if team notification attempted removing an enemy from the hostage list.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "HOSTAGE_REMOVAL_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "An enemy piece cannot be removed from the team's hostage list."

#======================# SEARCH EXCEPTIONS #======================#  
class RosterNumberOutOfBoundsException(TeamException, SearchException):
  """Attempting to old_search for team roster number < 1 or > team_size raises an rollback_exception."""
  ERROR_CODE = "ROSTER_NUMBER_OUT_OF_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "Roster numbers are in the range [1, team_size]. Search failed."






