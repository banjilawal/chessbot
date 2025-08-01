from chess.common.exceptions import ChessException


class ValidationException(ChessException):
    default_message = "The validation failed."