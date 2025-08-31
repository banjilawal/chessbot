from assurance.exception.base import AssuranceException


class ConflictingEventStateException(AssuranceException):
    ERROR_CODE = "PERMISSION_CONSTRUCTION_ERROR"
    DEFAULT_MESSAGE = f"Cannot construct a Permission object with both PERMISSION and exception params not null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"