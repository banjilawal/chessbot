class LongNameException(ChessException):
    """
    Name is longer than MAX_NAME_LENGTH raises LongNameException. See documentation
    pr chess.common.config for MAX_NAME_LENGTH
    """

    ERROR_CODE = "LONG_NAME_ERROR"
    DEFAULT_MESSAGE = "Name is above the maximum length"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"