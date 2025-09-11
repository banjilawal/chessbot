from chess.exception.null_exception import NullException


class NullTeamProfileException(NullException):
    """
    Raised if a null TeamProfile is passed to Team.__init__.
    """

    ERROR_CODE = "NULL_SIDE_PROFILE_ERROR"
    DEFAULT_MESSAGE = f"TeamProfile cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"