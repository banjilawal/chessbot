from chess.exception.id import ChessException


class ValidationException(ChessException):
    default_message = "The validators failed."