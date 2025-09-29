

# === ===

class RequestValidationException(ValidationException):
    ERROR_CODE = "REQUEST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"request validation failed"



class AttackRequestValidationException(RequestValidationException):
    ERROR_CODE = "ATTACK_REQUEST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"AttackRequest validation failed"



class PromotionRequestValidationException(RequestValidationException):
    ERROR_CODE = "PROMOTION_REQUEST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"PromotionRequest validation failed"



class ExitRequestValidationException(RequestValidationException):
    ERROR_CODE = "EXIT_REQUEST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"ExitRequest validation failed"







