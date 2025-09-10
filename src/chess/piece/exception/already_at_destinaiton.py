class AlreadyAtDestinationException(PieceException):
    """
    If a piece's destination is its current position raise AlreadyAtDestination.
    """

    ERROR_CODE = "ALREADY_AT_DESTINATION_ERROR"
    DEFAULT_MESSAGE = "Piece is already at the destination."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"