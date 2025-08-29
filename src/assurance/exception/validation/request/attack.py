
from assurance.exception.validation.request.base import RequestValidationException


class AttackRequestValidationException(RequestValidationException):
    ERROR_CODE = "ATTACK_REQUEST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"AttackRequest validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
