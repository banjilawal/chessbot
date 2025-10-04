from chess.system import InconsistentCollectionException
from chess.system.err import (
    ChessException, NullException, ValidationException, FailedBuildException, CollectionException
)

__all__ = [
    'CommanderException',

# === COMMANDER VALIDATION EXCEPTIONS ===
    'NullCommanderException',
    'InvalidCommanderException',

# === COMMANDER BUILD EXCEPTIONS ===
    'CommanderBuildFailedException',

# === COMMANDER HISTORY EXCEPTIONS ===
    'CommanderHistoryException',
    'InvalidCommanderAssignmentException',
    'TeamListValidationException'
]

class CommanderException(ChessException):
    """
    Super class for exceptions raised by Commander objects. DO NOT USE DIRECTLY. Subclasses give more useful debugging
    messages.
    """
    ERROR_CODE = "COMMANDER_ERROR"
    DEFAULT_MESSAGE = "Commander raised an team_exception"

# === COMMANDER VALIDATION EXCEPTIONS ===
class NullCommanderException(CommanderException, NullException):
    """
    Raised if a commander is null.
    """
    ERROR_CODE = "NULL_COMMANDER_ERROR"
    DEFAULT_MESSAGE = f"Commander cannot be null"

class InvalidCommanderException(CommanderException, ValidationException):
    ERROR_CODE = "COMMANDER_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Commander validate failed"

# === COMMANDER BUILD EXCEPTIONS ===
class CommanderBuildFailedException(CommanderException, FailedBuildException):
    """
    CommanderBuilder exceptions.
    """
    ERROR_CODE = "COMMANDER_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Commander build failed."

# === COMMANDER HISTORY EXCEPTIONS ===
class CommanderHistoryException(CommanderException):
    """Team list specific errors."""
    ERROR_CODE = "COMMANDER_HISTORY_ERROR"
    DEFAULT_MESSAGE = "CommanderHistory raised an exception."

class InconsistentCommandHistoryException(CommanderHistoryException, InconsistentCollectionException):
    ERROR_CODE = "INCONSISTENT_COMMANDER_HISTORY_ERROR"
    DEFAULT_MESSAGE = (
        "CommanderHistory is an inconsistent state. Data might be corrupt."
    )

class AddNewTeamException(TeamRosterException):
    """Raised if a new team could not be added to commandHistory"""
    ERROR_CODE = "ADD_NEW_TEAM_ERROR"
    DEFAULT_MESSAGE = "Could not add a new team to CommandHistory."

class RemoveNewTeamException(TeamRosterException):
    """Raised an undo push_team commandHistory"""
    ERROR_CODE = "REMOVE_NEW_TEAM_ERROR"
    DEFAULT_MESSAGE = "Could not remove the new team from CommandHistory."

class AddEnemyToRosterException(TeamRosterException):
    """Attempting to add an enemy to the team's roster raises an err"""
    ERROR_CODE = "ADD_ENEMY_TO_ROSTER_ERROR"
    DEFAULT_MESSAGE = "An enemy piece cannot be added to the team's roster"

class CannotRemoveOldTeamException(TeamRosterException):
    """Raised if an attempt is made to remove an old team from CommandHistory"""
    ERROR_CODE = "REMOVE_OLD_TEAM_ERROR"
    DEFAULT_MESSAGE = "Removing old teams from CommandHistory is not allowed."

class InvalidCommanderAssignmentException(CommanderHistoryException):
    """
    If a team already attached to a commander (team.commander == not None) tries being assigned a
    different commander, `InvalidCommanderAssignmentException` is raised.
    """
    ERROR_CODE = "INVALID_COMMANDER_ASSIGNMENT_ERROR"
    DEFAULT_MESSAGE = "Team is already assigned to a different commander."




