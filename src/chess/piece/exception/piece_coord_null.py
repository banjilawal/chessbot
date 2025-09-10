class PieceCoordNullException(PieceException):
    """
    PieceCoordNullException gets thrown if a piece with an empty coord stack attempts to move.
    If piece.positions.is_empty == True then the piece is not on the board so it cannot be moved.
    """

    ERROR_CODE = "PIECE_NO_COORDINATE_ERROR"
    DEFAULT_MESSAGE = "Piece is not on the board. Cannot move a piece with len(piece.positions) == 0"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

















