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

