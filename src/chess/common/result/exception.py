
from chess.exception import ChessException

__all__ = [
    'ResultPayloadConflictException'
]

class ResultPayloadConflictException(ChessException):
    """Raised if both payload and exception params are not null when constructing a Result object"""
    ERROR_CODE = "RESULT_CONSTRUCTOR_ERROR"
    DEFAULT_MESSAGE = f"Cannot construct a Result object with both payload and exception params not null"