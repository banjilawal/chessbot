from assurance.exception.base import AssuranceException


class EmptyConstructorException(AssuranceException):
    ERROR_CODE = "EMPTY_ASSURANCE_ENTITY_CONSTRUCTOR"
    DEFAULT_MESSAGE = f"All constructor params cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
