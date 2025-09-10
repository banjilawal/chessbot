from .chess_exception import ChessException

class SearchException(ChessException):
    """
    If a search caller get null back then it raises a SearchException. Searches are for a
    specific instance of an object. Raise the SearchException which matches the object.

    Subclass Naming Rule:
        <Class>NotFoundException
    """

    ERROR_CODE = "SEARCH_ERROR"
    DEFAULT_MESSAGE = "Search raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


