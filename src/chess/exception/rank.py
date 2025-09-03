from chess.exception.base import ChessException


class RankException(ChessException):
    ERROR_CODE = "RANK_ERROR"
    DEFAULT_MESSAGE = "Rank raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class UnPromotableRankException(RankException):
    ERROR_CODE = "UNPROMOTABLE_RANK_PROMOTION_ERROR"
    DEFAULT_MESSAGE = "Rank is not promotable"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PromotionRowException(RankException):
    ERROR_CODE = "PROMOTION_ROW_ERROR"
    DEFAULT_MESSAGE = "Incorrect row for rank promotion"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PawnRankException(RankException):
    ERROR_CODE = "PAWN_RANK_ERROR"
    DEFAULT_MESSAGE = "PawnRank raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class KingRankException(RankException):
    ERROR_CODE = "KING_RANK_ERROR"
    DEFAULT_MESSAGE = "KingRank raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class KnightRankException(RankException):
    ERROR_CODE = "KNIGHT_RANK_ERROR"
    DEFAULT_MESSAGE = "KnightRank raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class BishopRankException(RankException):
    ERROR_CODE = "BISHOP_RANK_ERROR"
    DEFAULT_MESSAGE = "BishopRank raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class CastleRankException(RankException):
    ERROR_CODE = "CASTLE_RANK_ERROR"
    DEFAULT_MESSAGE = "CastleRank raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class QueenRankException(RankException):
    ERROR_CODE = "QUEEN_RANK_ERROR"
    DEFAULT_MESSAGE = "QuenRank raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



