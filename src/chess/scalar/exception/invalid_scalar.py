from assurance.exception.validation_exception import ValidationException


class ScalarValidationException(ValidationException):
    ERROR_CODE = "SCALAR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Scalar validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
