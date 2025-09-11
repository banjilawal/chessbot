
class PawnValidationException(ValidationException):
    ERROR_CODE = "PAWN_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Pawn validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
