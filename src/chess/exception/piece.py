from chess.exception.base import ChessException


class PieceException(ChessException):
    ERROR_CODE = "PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PieceCoordinateException(PieceException):
    ERROR_CODE = "PIECE_NO_COORDINATE_ERROR"
    DEFAULT_MESSAGE = "Piece is not on the board. it has no coordinate"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PrisonerEscapeException(PieceException):
    ERROR_CODE = "CAPTURED_PIECE_ESCAPE_ERROR"
    DEFAULT_MESSAGE = "A captured piece cannot move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingNullPieceException(PieceException):
    ERROR_CODE = "ATTACKING_NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot capture a null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingPrisonerException(PieceException):
    ERROR_CODE = "ATTACKING_CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot capture a piece already captured"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingKingException(PieceException):
    ERROR_CODE = "ATTACKING_KING_EXCEPTION"
    DEFAULT_MESSAGE = "Cannot capture a king"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingFriendlyException(PieceException):
    ERROR_CODE = "ATTACKING_FRIENDLY_ERROR"
    DEFAULT_MESSAGE = "Cannot attack a friendly"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class DoublePromotionException(PieceException):

    """
    Only a piece can be doubly promoted. DoublePromotionException is a PieceException
    not a RankException.
    """

    ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
    DEFAULT_MESSAGE = "Piece is already promoted. It cannot be promoted again"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class KingCheckStateException(PieceException):
    ERROR_CODE = "KING_CHECK_STATE"
    DEFAULT_MESSAGE = "A dead piece cannot attack"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

class KingCheckMateStateException(PieceException):
    ERROR_CODE = "KING_CHECKMATE_STATE"
    DEFAULT_MESSAGE = "King checkmated"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"