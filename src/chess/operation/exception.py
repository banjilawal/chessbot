from chess.exception import ChessException, ValidationException, NullException

__all__ = [
    'OperationException',
    'OperationExecutorException',
    'DirectiveException',
    'InvalidDirectiveException',

    'NullOperationException',
    'NullOperationExecutorException',
    'NullDirectiveException',
    'NullDirectiveException'
]

class OperationException(ChessException):
    ERROR_CODE = "OPERATION_ERROR"
    DEFAULT_MESSAGE = "Operation raised an error"

class OperationExecutorException(OperationException):
    ERROR_CODE = "OPERATION_EXECUTOR_ERROR"
    DEFAULT_MESSAGE = "OperationExecutor raised an error"

class DirectiveException(OperationException):
    ERROR_CODE = "DIRECTIVE_ERROR"
    DEFAULT_MESSAGE = "Directive raised an error"

class InvalidDirectiveException(ValidationException):
    ERROR_CODE = "INVALID_DIRECTIVE_ERROR"
    DEFAULT_MESSAGE = "Directive validation failed"

class NullOperationException(NullException):
    ERROR_CODE = "NULL_OPERATION_ERROR"
    DEFAULT_MESSAGE = "Operation cannot be null"

class NullOperationExecutorException(OperationExecutorException, NullOperationException):
    ERROR_CODE = "NULL_OPERATION_EXECUTOR_ERROR"
    DEFAULT_MESSAGE = "OperationExecutor cannot be null"

class NullDirectiveException(NullOperationException):
    ERROR_CODE = "NULL_DIRECTIVE_ERROR"
    DEFAULT_MESSAGE = "Directive cannot be null"

class NullDirectiveValidatorException(DirectiveValidationException, NullOperationException):
    ERROR_CODE = "NULL_DIRECTIVE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Directive validation failed"
"

