from chess.system import(
    ChessException,
    NullException,
    FailedBuildException,
    ValidationException,
    InconsistentCollectionException
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
    DEFAULT_MESSAGE = "Commander raised an team_exception"

# === COMMANDER VALIDATION EXCEPTIONS ===
class NullCommanderException(CommanderException, NullException):
    """Raised if an entity, method, or operation requires a commander but gets null instead."""
    ERROR_CODE = "NULL_COMMANDER_ERROR"
    DEFAULT_MESSAGE = f"Commander cannot be null"

class InvalidCommanderException(CommanderException, ValidationException):
    """
    Raised by BoardValidator if board fails sanity checks. Exists primarily to catch all exceptions raised
    validating an existing board
    """
    ERROR_CODE = "COMMANDER_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Commander validate failed"

# === COMMANDER BUILD EXCEPTIONS ===
class CommanderBuildFailedException(CommanderException, FailedBuildException):
    """
    Raised when BoardBuilder encounters an error while building a team. Exists primarily to catch all
    exceptions raised build a new board
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

class PushNewTeamException(CommanderHistoryException):
    """Raised if a new team could not be pushed to commandHistory"""
    ERROR_CODE = "PUSH_NEW_TEAM_ERROR"
    DEFAULT_MESSAGE = "Could not push a new team to CommandHistory."

class UndoingPushTeamFailedException(CommanderHistoryException):
    """Raised if removing the current team failed"""
    ERROR_CODE = "UNDOING_PUSH_TEAM_FAILED_ERROR"
    DEFAULT_MESSAGE = "Could not undo the new team addition."

class CannotRemoveOldTeamException(CommanderHistoryException):
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




