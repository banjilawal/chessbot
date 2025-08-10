from chess.common.chess_exception import ChessException


class ValidationException(ChessException):
    default_message = "The validation failed."