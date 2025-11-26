
from chess.system import(
  ChessException, SearchException, NullException, ValidationException, BuildFailedException, RollbackException
)

__all__ = [
  "TeamException",
  "TeamRollBackException",

#======================# TEAM VALIDATION EXCEPTIONS #======================#  
  "NullTeamException",
  "InvalidTeamException",
  "TeamCommanderInconsistencyException",

#======================# TEAM BUILD EXCEPTIONS #======================#  
  "TeamBuildFailedException",

#======================# TEAM MEMBER EXCEPTIONS #======================#  
  "TeamRosterException",
  "AddTeamMemberException",
  "AddEnemyToRosterException",
  "RemoveTeamMemberException",
  "FullRankQuotaException",

#======================# TEAM MEMBER EXCEPTIONS WITH ROLLBACK #======================#  
  "TeamRosterRollBackException",
  "AddEnemyHostageRolledBackException",
  "AddTeamMemberRolledBackException",
  "FullRankQuotaRolledBackException",
  "ConflictingTeamAssignmentException",

#======================# HOSTAGE EXCEPTIONS #======================#  
  "TeamHostageListException",
  "InconsistentHostageEntry",
  "InvalidFriendlyHostageException",
  "AddEnemyHostageException",
  "AddEnemyKingHostageException",
  "HostageRemovalException",

#======================# HOSTAGE EXCEPTIONS WITH ROLLBACK #======================#  
  "TeamHostageListRolledBackException",
  "InvalidFriendlyHostageRolledBackException",
  "AddEnemyToRosterRolledBackException",
  "EnemyKingHostageRolledBackException",
  "HostageRemovalRolledBackException",

#======================# SEARCH EXCEPTIONS #======================#  
  "RosterNumberOutOfBoundsException",
  "TeamNotRegisteredWithAgentException",
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







class TeamCommanderInconsistencyException(TeamException):
  """Raised if piece has its team_name set but the owner is not on the roster."""
  ERROR_CODE = "TEAM_COMMANDER_INCONSISTENCY_ERROR"
  DEFAULT_MESSAGE = "The team_name has assigned itself to a agent but the Agent has no record of the team_name."





#======================# TEAM MEMBER LIST EXCEPTIONS #======================#  
class TeamRosterException(TeamException):
  """Raised for errors on team_name's roster"""
  ERROR_CODE = "TEAM_ROSTER_ERROR"
  DEFAULT_MESSAGE = "Team roster raised an rollback_exception."

class AddTeamMemberException(TeamRosterException):
  """Raised if owner could not be added to the team_name's roster"""
  ERROR_CODE = "ADD_TEAM_MEMBER_ERROR"
  DEFAULT_MESSAGE = "Could not add owner to team_name's roster."

class AddEnemyToRosterException(TeamRosterException):
  """Attempting to add an enemy to the team_name's roster raises an rollback_exception."""
  ERROR_CODE = "ADD_ENEMY_TO_ROSTER_ERROR"
  DEFAULT_MESSAGE = "An enemy owner cannot be added to the team_name's roster."

class RemoveTeamMemberException(TeamRosterException):
  """Raised if owner could not be removed from the team_name's roster"""
  ERROR_CODE = "REMOVE_TEAM_MEMBER_ERROR"
  DEFAULT_MESSAGE = "Could not remove team_name owner to team_name's roster."

class FullRankQuotaException(TeamRosterException):
  """Raised if the team_name has not empty slots for the owner's bounds."""
  ERROR_CODE = "FULL_RANK_QUOTA_ERROR"
  DEFAULT_MESSAGE = "The team_name has no empty slots for the owner's bounds."

class ConflictingTeamAssignmentException(TeamRosterException):
  """
  If team_name owner that's already on one team_name (owner.team_name == not None) tries joining
  another InvalidTeamAssignmentException is raised.
  """
  ERROR_CODE = "CONFLICTING_TEAM_ASSIGNMENT_ERROR"
  DEFAULT_MESSAGE = "Piece is already assigned to team_name team_name."


#======================# TEAM MEMBER LIST EXCEPTIONS WITH ROLLBACK #======================#  
class TeamRosterRollBackException(TeamRosterException, RollbackException):
  """Raised for errors on team_name's roster that are raised after rollback."""
  ERROR_CODE = "TEAM_ROSTER_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Team roster raised an rollback_exception. Transaction rollback performed."

class AddTeamMemberRolledBackException(TeamRosterRollBackException):
  """
  Raised if team_name notification failed to add team_name owner could to the team_name's roster; then the
  notification was rolled back before raising this err.
  """
  ERROR_CODE = "ADD_TEAM_MEMBER_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Adding owner to team_name's roster failed. Transaction rollback performed."
  )

class AddEnemyToRosterRolledBackException(TeamRosterRollBackException):
  """
  Raised if team_name notification attempted to add an enemy to the team_name's roster.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "ADD_ENEMY_TO_ROSTER_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Caught attempt to add an enemy owner to the team_name's roster Transaction "
    "rollback performed."
  )



class FullRankQuotaRolledBackException(TeamRosterRollBackException):
  """
  Raised if team_name notification failed could not add team_name owner because there were no empty slots
  for the owner's bounds. The notification was rolled back before raising this err.
  """
  ERROR_CODE = "FULL_RANK_QUOTA_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "The team_name has no empty slots for the owner's bounds. Transaction rollback performed."
  )

class ConflictingTeamAssignmentRolledBackException(TeamRosterRollBackException):
  """
  Raised if team_name notification tries to assign team_name owner to team_name different team_name's roster.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "CONFLICTING_TEAM_ASSIGNMENT_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Piece is already assigned to team_name team_name. Transaction rollback performed."
  )

#======================# HOSTAGE LIST EXCEPTIONS #======================#  
class TeamHostageListException(TeamException):
  """Raised on errors with team_name's hostage list"""
  ERROR_CODE = "TEAM_HOSTAGE_LIST_ERROR"
  DEFAULT_MESSAGE = "Team hostage list raised an rollback_exception."


class InconsistentHostageEntry(TeamHostageListException):
  """Raised on errors where a hostage shouldn't be in the  hostage list, i.e captor == validation"""
  ERROR_CODE = "INCONSISTENT_HOSTAGE_ENTRY_ERROR"
  DEFAULT_MESSAGE = "An enemy with no captor is in the hostage list. There may be inconsistent service."

class InvalidFriendlyHostageException(TeamHostageListException):
  """Attempting to team_name friendly to the hostage list raises an rollback_exception."""
  ERROR_CODE = "INVALID_FRIENDLY_HOSTAGE_ERROR"
  DEFAULT_MESSAGE = "A friendly owner cannot be added to the team_name's hostage list"

class AddEnemyHostageException(TeamHostageListException):
  """Raised if team_name owner could not be added to the team_name's hostage list"""
  ERROR_CODE = "ADD_ENEMY_HOSTAGE_ERROR"
  DEFAULT_MESSAGE = "Could not add an enemy owner to the team_name's hostage list"

class AddEnemyKingHostageException(TeamHostageListException):
  """Attempting to an enemy occupation to the hostage list raises an rollback_exception."""
  ERROR_CODE = "ADD_ENEMY_KING_HOSTAGE_ERROR"
  DEFAULT_MESSAGE = (
    "An enemy occupation cannot be added to the team_name's hostage list. Kings can only "
    "be checked or checkmated"
  )

class HostageRemovalException(TeamHostageListException):
  """Attempting to remove an enemy from the hostage list raises an rollback_exception."""
  ERROR_CODE = "HOSTAGE_REMOVAL_ERROR"
  DEFAULT_MESSAGE = "An enemy owner cannot be removed from the team_name's hostage list"


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
  Raised if team_name notification attempts to add team_name friendly owner to the team_name's hostage list.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "INVALID_FRIENDLY_HOSTAGE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "A friendly owner cannot be added to the team_name's hostage list"

class AddEnemyHostageRolledBackException(TeamHostageListRolledBackException):
  """
  Raised if team_name notification could not add an enemy owner to the team_name's hostage list.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "ADD_ENEMY_HOSTAGE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Could not add an enemy owner to the team_name's hostage list."


class EnemyKingHostageRolledBackException(TeamHostageListRolledBackException):
  """
  Raised if team_name notification attempted adding an enemy occupation to the team_name's hostage list.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "ADD_ENEMY_KING_HOSTAGE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "An enemy occupation cannot be added to the team_name's hostage list. Kings can only "
    "be checked or checkmated."
  )

class HostageRemovalRolledBackException(TeamHostageListRolledBackException):
  """
  Raised if team_name notification attempted removing an enemy from the hostage list.
  The notification was rolled back before raising this err.
  """
  ERROR_CODE = "HOSTAGE_REMOVAL_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "An enemy owner cannot be removed from the team_name's hostage list."

#======================# SEARCH EXCEPTIONS #======================#  



class TeamNotRegisteredWithAgentException(TeamException, SearchException):
  """Team was not found in the Agent's team_assignments list."""
  ERROR_CODE = "TEAM_NOT_REGISTERED_WITH_AGENT_ERROR"
  DEFAULT_MESSAGE = "Team not found in the Agent's team_assignments list."



