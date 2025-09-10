class DoublePromotionException(PieceException):
    """
    If a piece with rank in [Pawn, King] has been promoted to Queen, DoublePromotionException
    is raised if there is a second attempt to promote the chess piece.
    """

    ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
    DEFAULT_MESSAGE = "Piece is already promoted to Queen. It cannot be promoted again"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"