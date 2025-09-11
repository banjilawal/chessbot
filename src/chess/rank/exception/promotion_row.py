from chess.exception import RankException

class PromotionRowException(RankException):
    ERROR_CODE = "PROMOTION_ROW_ERROR"
    DEFAULT_MESSAGE = "Incorrect row for validation promotion"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"