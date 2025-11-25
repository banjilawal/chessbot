
from chess.team import TeamException
from chess.system import ValidationException

class InvalidTeamException(TeamException, ValidationException):
    """Catchall Exception for TeamValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "TEAM_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Team validation failed."