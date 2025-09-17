from chess.exception import ChessException

class ResultPayloadConflictException(ChessException):
    ERROR_CODE = "RESULT_CONSTRUCTOR_ERROR"
    DEFAULT_MESSAGE = f"Cannot construct a Result object with both payload and exception params not null"