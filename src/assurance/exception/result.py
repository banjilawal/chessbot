from assurance.exception.base import AssuranceException


class ResultPayloadConflictException(AssuranceException):
    ERROR_CODE = "RESULT_CONSTRUCTOR_ERROR"
    DEFAULT_MESSAGE = f"Cannot construct a Result object with both payload and exception params not null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"