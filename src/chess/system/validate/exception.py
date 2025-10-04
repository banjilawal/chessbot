from chess.system import ChessException

__all__ = ['ValidationException']

class ValidationException(ChessException):
    ERROR_CODE = "VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Validation failed."


