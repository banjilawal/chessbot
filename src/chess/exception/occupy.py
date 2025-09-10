from chess.exception.chess_exception import ChessException


class OccupationException(ChessException):
    ERROR_CODE = "OCCUPATION_ERROR"
    DEFAULT_MESSAGE = "An occupation exception was raised"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class OccupyNullSquareException(ChessException):
    ERROR_CODE = "OCCUPY_NULL_SQUARE_EXCEPTION"
    DEFAULT_MESSAGE = "Cannot occupy a square which does not exist"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class FriendlyOccupantException(OccupationException):
    ERROR_CODE = "FRIENDLY_OCCUPANT_ERROR"
    DEFAULT_MESSAGE = "A friendly is already occupying the square"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class OccupiedBySelfException(OccupationException):
    ERROR_CODE = "OCCUPIED_BY_SELF_ERROR"
    DEFAULT_MESSAGE = "You are already occupying the square"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
