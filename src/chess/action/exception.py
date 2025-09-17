from chess import ChessException, ValidationException

__all__ = [
    'ExecutionException',
    'DirectiveValidationException',

    'OccupationExecutionException',
    'OccupationValidationException'

]

class ExecutionException(ChessException):
    ERROR_CODE = "EXECUTION_ERROR"
    DEFAULT_MESSAGE = "Execution operation raised an error"


class DirectiveValidationException(ValidationException):
    """Directive exceptions."""

    ERROR_CODE = "DIRECTIVE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Directive validation failed"


class OccupationExecutionException(ChessException):
    ERROR_CODE = "OCCUPATION_EXECUTION_ERROR"
    DEFAULT_MESSAGE = "An exception was raised while executing the square occupation "


class OccupationValidationException(ValidationException):
    """OccupationDirective validation failure."""

    ERROR_CODE = "OCCUPATION_DIRECTIVE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "OccupationDirective failed validation"