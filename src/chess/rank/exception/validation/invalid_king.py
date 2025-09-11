
class KingValidationException(ValidationException):
    ERROR_CODE = "KING_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"King validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
