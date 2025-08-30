from assurance.exception.validation.base import ValidationException


class RequestValidationException(ValidationException):
    ERROR_CODE = "REQUEST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"request validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackRequestValidationException(RequestValidationException):
    ERROR_CODE = "ATTACK_REQUEST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"AttackRequest validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class OccupationRequestValidationException(RequestValidationException):
    ERROR_CODE = "OCCUPATION_REQUEST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"OccupationRequest validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PromotionRequestValidationException(RequestValidationException):
    ERROR_CODE = "PROMOTION_REQUEST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"PromotionRequest validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ExitRequestValidationException(RequestValidationException):
    ERROR_CODE = "EXIT_REQUEST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"ExitRequest validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"