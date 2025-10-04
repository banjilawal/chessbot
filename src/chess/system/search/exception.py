from chess.system import ChessException

__all__ = [
    'SearchException',
    'SearchParamException',
    'ImpossibleFatalResultException'
]

class SearchException(ChessException):
    """
    Base class for search errors in the chess engine.

    PURPOSE:
        Raised search raises an err. Is a wrapper for other exceptions
        that occur during search.
    ATTRIBUTES:
        code (str): Short machine-readable err code for logging / testing.
        message (str): Human-readable default message.
    """
    DEFAULT_CODE = "SEARCH_ERROR"
    DEFAULT_MESSAGE = "Search raised an err."


class SearchParamException(SearchException):
    DEFAULT_CODE = "SEARCH_PARAM_ERROR"
    DEFAULT_MESSAGE = "Search parameters "


class ImpossibleFatalResultException(SearchException):
    DEFAULT_CODE = "IMPOSSIBLE_FATAL_RESULT_ERROR"
    DEFAULT_MESSAGE = (
        "The search result should be impossible. The result "
        "indicates a major data inconsistency or system error"
    )








