
class QueenValidationException(ValidationException):
    ERROR_CODE = "QUEEN_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Queen validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
