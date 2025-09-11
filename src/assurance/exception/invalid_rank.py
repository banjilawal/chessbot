from assurance.exception.validation_exception import ValidationException


class RankValidationException(ValidationException):
    ERROR_CODE = "RANK_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Rank validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
