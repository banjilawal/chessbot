from chess import CollectionException
from chess.exception import ChessException, NullException, ValidationException, BuilderException

__all__ = [
    'CommanderException',
    'NullCommanderException',
    'CommanderBuilderException',
    'CommanderValidationException',

    'TeamListException',
    'TeamListValidationException'
]

"""
Super class for Commander exceptions and TeamList exceptions
"""

class CommanderException(ChessException):
    """
    Super class for exceptions raised by Piece objects
    """
    ERROR_CODE = "COMMANDER_ERROR"
    DEFAULT_MESSAGE = "Commander raised an team_exception"


class CommanderBuilderException(BuilderException):
    """
    CommanderBuilder exceptions.
    """
    ERROR_CODE = "COMMANDER_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CommanderBuilder raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class NullCommanderBuilderException(NullException):
    """
    Raised if a CommanderBuilder is null.
    """

    ERROR_CODE = "NULL_COMMANDER_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CommanderBuilder cannot be null"


class NullCommanderException(NullException):
    """
    Raised if a commander is null.
    """
    ERROR_CODE = "NULL_COMMANDER_ERROR"
    DEFAULT_MESSAGE = f"Commander cannot be null"


class CommanderValidationException(ValidationException):
    ERROR_CODE = "COMMANDER_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Commander validation failed"






class TeamListException(CollectionException):
    """Team list specific errors."""
    ERROR_CODE = "TEAM_LIST_ERROR"
    DEFAULT_MESSAGE = "Team list operation failed"


class TeamListValidationException(ValidationException):
    ERROR_CODE = "TEAM_LIST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"TeamList validation failed"
