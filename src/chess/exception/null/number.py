from chess.exception.null.base import NullException


class NullNumberException(NullException):
    """
    Raised if mathematical expression or geometric, algebraic, or optimization that need
     a number but get null instead NUllNumberException is thrown. Ids are not used for math
     so we need a different null exception for math variables
    """

    ERROR_CODE = "NULL_NUMBER_ERROR"
    DEFAULT_MESSAGE = f"Number cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"