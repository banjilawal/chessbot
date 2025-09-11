from chess.exception import RankException

class UnPromotableException(RankException):
    ERROR_CODE = "UNPROMOTABLE_RANK_PROMOTION_ERROR"
    DEFAULT_MESSAGE = "Rank is not promotable"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"