from chess.exception.null.base import NullException


class NullStringException(NullException):
    """
    Raised if search parameter is a null string
    """

    ERROR_CODE = "NULL_STRING_SEARCH_ERROR"
    DEFAULT_MESSAGE = f"Cannot search by a null string"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"