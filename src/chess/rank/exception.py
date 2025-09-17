from chess.exception import ChessException

__all__ = [

    # Super class for exceptions occurring with Rank responsibilities
    'RankException',

    # Exceptions for invalid moves
    'KingMovingException',
    'PawnMovingException',
    'KnightMovingException',
    'BishopMovingException',
    'RookMovingException',
    'QueenMovingException',

    # Specific rank validation exceptions
    'KingValidationException',
    'PawnValidationException',
    'KnightValidationException',
    'BishopValidationException',
    'RookValidationException',
    'QueenValidationException'
]

class RankException(ChessException):
    ERROR_CODE = "RANK_ERROR"
    DEFAULT_MESSAGE = "Rank raised an team_exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class BishopMovingException(RankException):
    ERROR_CODE = "BISHOP_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid bishop move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

class KingMovingException(RankException):
    ERROR_CODE = "KING_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid king move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class KnightMovingException(RankException):
    DEFAULT_MESSAGE = "Invalid knight move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PawnMovingException(RankException):
    ERROR_CODE = "PAWN_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid pawn move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class QueenMovingException(RankException):
    ERROR_CODE = "QUEEN_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid queen move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class RookMovingException(RankException):
    ERROR_CODE = "ROOK_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid rook move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class RankValidationException(ValidationException):
    ERROR_CODE = "RANK_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Rank validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class BishopValidationException(ValidationException):
    ERROR_CODE = "BISHOP_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Bishop validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class KingValidationException(ValidationException):
    ERROR_CODE = "KING_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"King validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class KnightValidationException(ValidationException):
    ERROR_CODE = "KNIGHT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Knight validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PawnValidationException(ValidationException):
    ERROR_CODE = "PAWN_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Pawn validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

class QueenValidationException(ValidationException):
    ERROR_CODE = "QUEEN_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Queen validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

class RookValidationException(ValidationException):
    ERROR_CODE = "ROOK_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Rook validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"