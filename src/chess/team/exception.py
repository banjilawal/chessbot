from chess.exception import ChessException, NullException, ValidationException, BuilderException

__all__ = [
    'TeamException',
    'RankQuotaFullException',
    'InvalidTeamAssignmentException',
    'TeamBuilderException',
    'NulTeamBuilderException',
    'TeamValidationException',
    'NullTeamException',
    'NullTeamProfileException'
]

class TeamException(ChessException):
    """
    Super class for team_exception raised by a Team object when its internal fields or methods
    """
    ERROR_CODE = "SIDE_ERROR"
    DEFAULT_MESSAGE = "Team raised an team_exception"
    
    
class TeamBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when teamBuilder runs.
    """
    ERROR_CODE = "TEAM_BUILDER_ERROR"
    DEFAULT_MESSAGE = "TeamBuilder raised an exception"


class NulTeamBuilderException(NullException):
    """
    Raised if a TeamBuilder is null.
    """
    ERROR_CODE = "NULL_TEAM_BUILDER_ERROR"
    DEFAULT_MESSAGE = "TeamBuilder cannot be null"


class AddPieceException(TeamException):
    """
    Raised if discovery could not be added to the team's roster
    """
    ERROR_CODE = "ADD_PIECE_ERROR"
    DEFAULT_MESSAGE = "Could not add the discovery, an team_exception was raised"


class RankQuotaFullException(TeamException):
    """
    Raised if the team has not empty slots for the discovery's rank.
    """
    ERROR_CODE = "RANK_QUOTA_FULL_ERROR"
    DEFAULT_MESSAGE = "The team has no empty slots for the discovery's rank"


class InvalidTeamAssignmentException(TeamException):
    """
    If a discovery that's already on one team (discovery.team == not None) tries joining
    another InvalidTeamAssignmentException is raised.
    """
    ERROR_CODE = "INVALID_TEAM_ASSIGNMENT_ERROR"
    DEFAULT_MESSAGE = "Piece is already assigned to a team."


class TeamValidationException(ValidationException):
    ERROR_CODE = "TEAM_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Team validation failed"


class NullTeamException(NullException):
    ERROR_CODE = "NULL_TEAM_ERROR"
    DEFAULT_MESSAGE = f"Team cannot be null"


class NullTeamProfileException(NullException):
    """
    Raised if a null TeamProfile is passed to Team.__init__.
    """
    ERROR_CODE = "NULL_SIDE_PROFILE_ERROR"
    DEFAULT_MESSAGE = f"TeamProfile cannot be null"




