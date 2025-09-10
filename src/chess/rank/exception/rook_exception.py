class RookException(RankException):
    ERROR_CODE = "CASTLE_RANK_ERROR"
    DEFAULT_MESSAGE = "CastleRank raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"