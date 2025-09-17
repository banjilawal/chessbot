from chess.exception import ChessException, NullException, ValidationException

class TeamException(ChessException):
    """
    Super class for team_exception raised by a Team object when its internal fields or methods
    """

    ERROR_CODE = "SIDE_ERROR"
    DEFAULT_MESSAGE = "Team raised an team_exception"


class AddPieceException(TeamException):
    """
    Raised if piece could not be added to the team's roster
    """

    ERROR_CODE = "ADD_PIECE_ERROR"
    DEFAULT_MESSAGE = "Could not add the piece, an team_exception was raised"


class InvalidTeamAssignmentException(TeamException):
    """
    If a piece that's already on one team (piece.team == not None) tries joining
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




