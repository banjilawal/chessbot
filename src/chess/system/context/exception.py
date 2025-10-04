from chess.system import ChessException


class ContextException(ChessException):
    """
    """
    ERROR_CODE = "CONTEXT_ERROR"
    DEFAULT_MESSAGE = "Context raised an exception."