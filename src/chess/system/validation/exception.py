from chess.exception import ChessException


class ValidationException(ChessException):
    ERROR_CODE = "VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Validation failed."


