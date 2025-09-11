from chess.exception.null_exception import NullException


class NullColumnException(NullException):
    """
    Raised if a column is null. A coord cannot be created if the column is null
    """

    ERROR_CODE = "NULL_COLUMN_ERROR"
    DEFAULT_MESSAGE=f"Column cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"