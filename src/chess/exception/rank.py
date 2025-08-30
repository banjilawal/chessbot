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



