from assurance.exception.validation.base_validation import ValidationException
from chess.exception.base.negative_id_exception import ChessException


class CoordinateValidationException(ValidationException):
    ERROR_CODE = "COORDINATE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Coordinate validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
