from assurance.exception.validation.base import ValidationException


class OwnerValidationException(ValidationException):
    ERROR_CODE = "OWNER_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Owner validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
