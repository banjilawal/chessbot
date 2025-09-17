class AssuranceException(Exception):
    ERROR_CODE = "ASSURANCE_ERROR"
    DEFAULT_MESSAGE = f"Assurance check failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ConflictingEventStateException(AssuranceException):
    ERROR_CODE = "PERMISSION_CONSTRUCTION_ERROR"
    DEFAULT_MESSAGE = f"Cannot construct a Permission object with both PERMISSION and exception params not null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class EmptyConstructorException(AssuranceException):
    ERROR_CODE = "EMPTY_ASSURANCE_ENTITY_CONSTRUCTOR"
    DEFAULT_MESSAGE = f"All constructor params cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class EmptyResultConstructorException(EmptyConstructorException):
    ERROR_CODE = "EMPTY_RESULT_CONSTRUCTOR_ERROR"
    DEFAULT_MESSAGE = f"Result constructor cannot have all null params"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class EmptyEventOutcomeConstructorException(EmptyConstructorException):
    ERROR_CODE = "MULTIPLE_NULL_CONSTRUCTOR_PARAM_ERROR"
    DEFAULT_MESSAGE = f"EventOutcome constructor cannot have both event and exception null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ValidationException(AssuranceException):
    ERROR_CODE = "VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class HostageValidationException(ValidationException):
    ERROR_CODE = "HOSTAGE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Hostage validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class IdValidationException(ValidationException):
    ERROR_CODE = "ID_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Id Validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class NameValidationException(ValidationException):
    ERROR_CODE = "NAME_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Name validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class RankValidationException(ValidationException):
    ERROR_CODE = "RANK_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Rank validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


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
