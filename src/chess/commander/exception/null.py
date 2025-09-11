from chess.exception.null_exception import NullException


class NullCommanderException(NullException):
    """
    Raised if a commander is null.
    """

    ERROR_CODE = "NULL_COMMANDER_ERROR"
    DEFAULT_MESSAGE = f"Commander cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"