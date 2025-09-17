from chess import ChessException, ValidationException

__all__ = [
    'OperationException',
    'ExecutionException',
]

class OperationException(ChessException):
    ERROR_CODE = "EXECUTION_ERROR"
    DEFAULT_MESSAGE = "Execution operation raised an error"

class ExecutionException(OperationException):
    ERROR_CODE = "EXECUTION_ERROR"
    DEFAULT_MESSAGE = "Execution operation raised an error"

