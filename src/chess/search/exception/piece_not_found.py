class PieceNotFoundException(SearchException):
    """
    Raised if a piece was not found in a search
    """

    ERROR_CODE = "PIECE_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = "The search did not find a piece"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"