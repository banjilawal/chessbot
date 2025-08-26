
from chess.exception.coordinate_stack.coord_stack import CoordinateStackException


class IsEmptyStackResultConflictsWithSizeException(CoordinateStackException):
    ERROR_CODE = "IS_EMPTY_STACK_RESULT_CONFLICTS_WITH_SIZE_ERROR"
    DEFAULT_MESSAGE = f"Results of CoordinateStack.is_empty() conflicts with CoordinateStack.size()."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



