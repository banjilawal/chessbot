
from assurance.exception.validation.request.base import RequestValidationException


class PromotionRequestValidationException(RequestValidationException):
    ERROR_CODE = "PROMOTION_REQUEST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"PromotionRequest validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
