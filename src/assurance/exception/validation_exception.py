from assurance.exception.assurance_exception import AssuranceException

class ValidationException(AssuranceException):
    ERROR_CODE = "VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
