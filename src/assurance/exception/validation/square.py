from assurance.exception.validation.base_validation import ValidationException


class SquareValidationException(ValidationException):
    ERROR_CODE = "SQUARE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Square validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ChessPieceValidationException(ValidationException):
    DEFAULT_MESSAGE = f"ChessPiece {ValidationException.DEFAULT_MESSAGE}"
