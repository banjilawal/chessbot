from chess.exception import ChessException


class ValidationException(ChessException):
    ERROR_CODE = "VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Validation failed"


