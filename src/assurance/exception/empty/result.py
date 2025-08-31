from assurance.exception.empty.base import EmptyConstructorException


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
