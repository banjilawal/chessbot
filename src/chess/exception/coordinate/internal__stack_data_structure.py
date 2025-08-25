from chess.exception.coordinate.coordinate_exception import CoordinateException


class InternalStackDataStructureException(CoordinateException):
    ERROR_CODE = "INTERNAL_STACK_DATA_STRUCTURE_ERROR"
    DEFAULT_MESSAGE = "The internal stack data structure is corrupted, null or invalid"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"