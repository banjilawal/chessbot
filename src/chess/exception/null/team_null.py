from chess.exception.null import NullException


class NullTeamException(NullException):
    default_message = f"Team {NullException.default_message}"