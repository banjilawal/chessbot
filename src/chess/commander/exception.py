from chess import CollectionException
from chess.exception import ChessException, NullException, ValidationException

__all__ = [
    'CommanderException',
    'NullCommanderException',
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
