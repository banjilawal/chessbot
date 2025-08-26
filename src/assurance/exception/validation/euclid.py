from assurance.exception.validation.base import ValidationException


class EuclideanDistanceValidationException(ValidationException):
    ERROR_CODE = "EUCLIDEAN_DISTANCE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Euclidean distance validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
