from chess.exception import RankException

class PawnException(RankException):
    ERROR_CODE = "PAWN_RANK_ERROR"
    DEFAULT_MESSAGE = "PawnRank raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"














