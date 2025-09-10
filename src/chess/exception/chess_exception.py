class ChessException(Exception):
    """
    Top level Exception for the chess application. ChessException is a template for
    other exceptions.

    Exception Requirements:
        - Static fields:
            ERROR_CODE (str): Must end in _ERROR. all caps summary of the exception or its cause
            DEFAULT_MESSAGE (str): Short sentence explaining what the exception is about.

        - A ChessException should always have a message describing the error.
    """

    ERROR_CODE = "CHESS_ERROR"
    DEFAULT_MESSAGE = "Chess error occurred"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
