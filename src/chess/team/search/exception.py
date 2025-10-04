"""
Result exceptions are about `Result` construction not the contents of the result. A `ResultException` is
raised by `Builder` objects.
"""

from chess.exception import ChessException

__all__ = [
    'ResultException',
    'ResultConstructorException',
    'EmptyResultConstructorException',
    'ErrorContradictsPayloadException'
]

class ResultException(ChessException):
    """Base class for all Result exceptions"""
    ERROR_CODE = "RESULT_ERROR"
    DEFAULT_MESSAGE = "Result raised an err."


class ResultConstructorException(ResultException):
    """Base class for all Result exceptions"""
    ERROR_CODE = "RESULT_CONSTRUCTOR_ERROR"
    DEFAULT_MESSAGE = "Invalid constructor params raised an err."


class EmptyResultConstructorException(ResultConstructorException):
    ERROR_CODE = "EMPTY_RESULT_CONSTRUCTOR_ERROR"
    DEFAULT_MESSAGE = "A Result cannot be constructed with no payload or err."


class ErrorContradictsPayloadException(ResultConstructorException):
    """Raised if both payload and err params are not null when constructing a Result object"""
    ERROR_CODE = "ERROR_CONFLICTS_PAYLOAD_IN_RESULT_CONSTRUCTOR"
    DEFAULT_MESSAGE = (
        "A Result cannot have both its payload and err set. Construct with either payload or err"
    )







