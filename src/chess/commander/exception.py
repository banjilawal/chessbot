from chess.exception import (
    ChessException, NullException, ValidationException, BuilderException, CollectionException
)

__all__ = [
    'CommanderException',
    'NullCommanderException',
    'CommanderBuilderException',
    'CommanderValidationException',
    'NullCommanderBuilderException',
    'InvalidCommanderAssignmentException',
    'TeamListException',
    'TeamListValidationException'
]

class CommanderException(ChessException):
    """
    Super class for exceptions raised by Piece objects
    """
    ERROR_CODE = "COMMANDER_ERROR"
    DEFAULT_MESSAGE = "Commander raised an team_exception"


class NullCommanderException(NullException):
    """
    Raised if a commander is null.
    """
    ERROR_CODE = "NULL_COMMANDER_ERROR"
    DEFAULT_MESSAGE = f"Commander cannot be null"


class CommanderValidationException(ValidationException):
    ERROR_CODE = "COMMANDER_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Commander validation failed"


class NullCommanderValidatorException(NullException):
    """
    Raised if a CommanderBuilder is null.
    """
    ERROR_CODE = "NULL_COMMANDER_VALIDATOR_ERROR"
    DEFAULT_MESSAGE = "CommanderValidator cannot be null"


class CommanderBuilderException(BuilderException):
    """
    CommanderBuilder exceptions.
    """
    ERROR_CODE = "COMMANDER_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CommanderBuilder raised an exception"


class NullCommanderBuilderException(NullException):
    """
    Raised if a CommanderBuilder is null.
    """
    ERROR_CODE = "NULL_COMMANDER_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CommanderBuilder cannot be null"


class InvalidCommanderAssignmentException(CommanderException):
    """
    If a team already attached to a commander (team.commander == not None) tries being assigned a
    different commander, `InvalidCommanderAssignmentException` is raised.
    """
    ERROR_CODE = "INVALID_COMMANDER_ASSIGNMENT_ERROR"
    DEFAULT_MESSAGE = "Team is already assigned to a commander."


class TeamListException(CollectionException):
    """Team list specific errors."""
    ERROR_CODE = "TEAM_LIST_ERROR"
    DEFAULT_MESSAGE = "Team list transaction failed"


class TeamListValidationException(ValidationException):
    ERROR_CODE = "TEAM_LIST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"TeamList validation failed"
