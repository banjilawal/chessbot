class SquareNotFoundException(SearchException):
    """
    Raised if a square was not found in a search
    """

    ERROR_CODE = "SQUARE_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = "The search did not find a square"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"