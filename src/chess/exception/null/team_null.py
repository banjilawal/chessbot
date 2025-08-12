from chess.exception.null.null import NullException


class NullTeamException(NullException):
    default_message = f"Team {NullException.default_message}"