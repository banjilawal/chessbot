from assurance.exception.validation.base_validation import ValidationException


class DistanceMagnitudeValidationException(ValidationException):
    ERROR_CODE = "DISTANCE_MAGNITUDE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"DistanceMagnitude validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
