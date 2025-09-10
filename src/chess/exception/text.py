from chess.exception.chess_exception import ChessException


class BlankStringException(ChessException):
    """
    Raised if search parameter is a blank or empty string
    """

    ERROR_CODE = "BLANK_SEARCH_STRING_ERROR"
    DEFAULT_MESSAGE = f"Cannot search by an empty or blank string"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"