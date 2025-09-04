from chess.exception.base import ChessException

class StackException(ChessException):
    ERROR_CODE = "STACK_ERROR"
    DEFAULT_MESSAGE = f"Stack raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class CorruptedStackException(StackException):
    ERROR_CODE = "INTERNAL_STACK_DATA_STRUCTURE_ERROR"
    DEFAULT_MESSAGE = "The internal stack data structure is corrupted, null or invalid"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class StackSizeConflictException(StackException):
    ERROR_CODE = "IS_EMPTY_STACK_RESULT_CONFLICTS_WITH_SIZE_ERROR"
    DEFAULT_MESSAGE = f"Stack.is_empty() conflicts with Stack.size()."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PopEmptyStackException(StackException):
    ERROR_CODE = "POP_EMPTY_STACK_EXCEPTION"
    DEFAULT_MESSAGE = f"Cannot pop an empty stack"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class DuplicatePushException(StackException):
    ERROR_CODE = "DUPLICATE_PUSH_STACK_ERROR"
    DEFAULT_MESSAGE = "Cannot push duplicate item onto the stack"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PushingNullEntityException(StackException):
    ERROR_CODE = "PUSHING_NULL_STACK_ERROR"
    DEFAULT_MESSAGE = "Cannot push a null coord onto the stack"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class BrokenRelationshipException(StackException):
    ERROR_CODE = "BROKEN_RELATIONSHIP_ERROR"
    DEFAULT_MESSAGE = "Broken bidirectional relationship"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


