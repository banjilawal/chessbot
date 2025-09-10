from chess.exception.chess_exception import ChessException

"""
Name with only white space raises this exception
"""
class WalkException(ChessException):
    ERROR_CODE = "WALK_ERROR"
    DEFAULT_MESSAGE = "Walk exception was raised"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class BishopWalkException(WalkException):
    ERROR_CODE = "BISHOP_WALK_ERROR"
    DEFAULT_MESSAGE = "BishopWalk unreachable destination"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class CastleWalkException(WalkException):
    ERROR_CODE = "CASTLE_WALK_ERROR"
    DEFAULT_MESSAGE = "CastleWalk unreachable destination"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class QueenWalkException(WalkException):
    ERROR_CODE = "QUEEN_WALK_ERROR"
    DEFAULT_MESSAGE = "QueenWalk unreachable destination"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class KnightWalkException(WalkException):
    ERROR_CODE = "KNIGHT_WALK_ERROR"
    DEFAULT_MESSAGE = "KnightWalk unreachable destination"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class KingWalkException(WalkException):
    ERROR_CODE = "KING_WALK_ERROR"
    DEFAULT_MESSAGE = "KingWalk unreachable destination"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PawnWalkException(WalkException):
    ERROR_CODE = "PAWN_WALK_ERROR"
    DEFAULT_MESSAGE = "PawnWalk unreachable destination"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"