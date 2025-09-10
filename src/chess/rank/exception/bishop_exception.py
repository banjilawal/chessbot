class BishopException(RankException):
    ERROR_CODE = "BISHOP_RANK_ERROR"
    DEFAULT_MESSAGE = "BishopRank raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"