from chess.exception.base import ChessException


class SearchException(ChessException):
    """
    If a search caller get null back then it raises a SearchException. Searches are for a
    specific instance of an object. Raise the SearchException which matches the object.

    Subclass Naming Rule:
        <Class>NotFoundException
    """

    ERROR_CODE = "SEARCH_ERROR"
    DEFAULT_MESSAGE = "Search failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class PieceNotFoundException(ChessException):
    """
    Raised if a piece was not found in a search
    """

    ERROR_CODE = "PIECE_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = "The search did not find a piece"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
