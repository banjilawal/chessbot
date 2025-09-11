class AddPieceException(TeamException):
    """
    Raised if piece could not be added to the team's roster
    """

    ERROR_CODE = "ADD_PIECE_ERROR"
    DEFAULT_MESSAGE = "Could not add the piece, an exception was raised"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

